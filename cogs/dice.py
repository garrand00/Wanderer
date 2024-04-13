import d20
import re

from custom_stringifier import BoolStringifier
from discord.ext import commands

ARITHMETIC_OPS = ["+", "-", "*", "/"]
BOOLEAN_OPS = ["=", "==", "<", "<=", ">", ">="]


# Cogs for Dice-Related command
class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.errorMsg = "Something is wrong. Please check your input"

    # Commands list
    @commands.Cog.listener()
    async def on_ready(self):
        print("dice.py loaded.")

    @commands.command(
        name="roll",
        description="command for rolling",
        aliases=["r"],
    )
    async def roll(self, ctx, *args):
        if len(args) < 1:
            await ctx.send("Please input a roll argument")
            return

        message = "<@{}> ".format(ctx.author.id) + self.resolve_bool_roll(args)
        await ctx.send(message)

    @commands.command(
        name="||roll",
        description="command for rolling, but spoiler-ed",
        aliases=["||r"],
    )
    async def roll_spoil(self, ctx, *args):
        if len(args) < 1:
            await ctx.send("Please input a roll argument")
            return

        print(self.resolve_bool_roll(args))
        message = "<@{}> ".format(ctx.author.id) + self.resolve_bool_roll(args)
        message = "||" + message.replace("||", "") + "||"
        await ctx.send(message)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or str(message.content[0]) == "`":
            return

        if self.find_inline_roll(message.content) and not (message.author.bot):
            inline_rolls = self.find_inline_roll(message.content)

            if len(inline_rolls) == 1 and "||" in inline_rolls[0]:
                reply = "||<@{}>||".format(message.author.id) 
            else:    
                reply = "<@{}> ".format(message.author.id) 

            if len(inline_rolls) > 1:
                reply += "\n"

            for x in inline_rolls:
                if "||" in x:
                    y = x.replace("||", "")
                    reply += (
                        "||"
                        + (
                            self.resolve_bool_roll(y.split()).replace(": ", "", 1)
                        )
                        + "||"
                    )
                else:
                    reply += (
                        self.resolve_bool_roll(x.split())
                    )
                
                reply += "\n"
            await message.channel.send(reply)

    # -----

    # Non-commands method
    def get_dice(self, roll, die=0):
        if die == 0:
            return d20.utils.dfs(roll.expr, lambda node: isinstance(node, d20.Dice))
        return d20.utils.dfs(
            roll.expr, lambda node: isinstance(node, d20.Dice) and node.size == die
        )

    def resolve_roll(self, args):
        try:
            parse = re.sub(" +", "", args[0])  # remove spaces
            comment = ""
            result = self._roll(parse)

            if len(args) > 1:
                comment = " ".join(args[1:])
            return comment + " : " + str(result)
        except Exception as e:
            return self.errorMsg

    def resolve_bool_roll(self, args):
        try:
            comment = ""
            parse = args[0]
            curOps = ""

            for ops in BOOLEAN_OPS:
                if ops in parse:
                    curOps = ops
                parse = re.sub(" " + ops, "", parse)  # remove spaces

            if curOps in BOOLEAN_OPS:
                target = int(parse.split(curOps, 1)[1])
                result, success = self._bool_roll(parse, curOps, target)

                if len(args) > 1:
                    comment = " ".join(args[1:])
                return comment + " : " + str(result) + " = " + str(success) + " success"
            else:
                return self.resolve_roll(args)
        except Exception as e:
            return self.resolve_roll(args)

    def _bool_roll(self, parse, curOps, target):
        try:
            success = 0

            # Handling = operator
            if curOps == "=":
                leftExp, rightExp = parse.split("=")
                parse = leftExp + "==" + rightExp

            result = d20.roll(parse, stringifier=BoolStringifier())
            dice = self.get_dice(result)

            if curOps in BOOLEAN_OPS:
                if dice is None:
                    raise Exception("No d6 dice found in the expression!")

                for die in dice.values:
                    if curOps == "=" or curOps == "==":
                        if die.number == target:
                            success = success + 1
                    if curOps == "<":
                        if die.number < target:
                            success = success + 1
                    if curOps == "<=":
                        if die.number <= target:
                            success = success + 1
                    if curOps == ">":
                        if die.number > target:
                            success = success + 1
                    if curOps == ">=":
                        if die.number >= target:
                            success = success + 1

                return result, success
            else:
                return self._roll(parse)
        except Exception as e:
            return self._roll(parse)

    def _roll(self, parse):
        try:
            result = d20.roll(parse)
            return result
        except Exception as e:
            return self.errorMsg


    def find_inline_roll(self, str):
        return re.findall(r"\[\[(.+?)\]\]", str)

    # -----


# cog setup
async def setup(client):
    await client.add_cog(Dice(client))