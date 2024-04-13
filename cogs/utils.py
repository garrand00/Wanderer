import discord
from discord.ext import commands

from tools.embed_builder import embed_builder

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("utils.py loaded.")

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.send(f"🏓 Wowzie! Latency: {bot_latency} ms.")

    @commands.command(name="eh-help")
    async def eh_help(self, ctx):
        help_data = {
            "title": "EH Help Bot",
            "fields": [
                {"name": "Class",
                "value": ";;eh-class",
                "inline": True},
                {"name": "Talent",
                "value": ";;eh-talent",
                "inline": True},
                {"name": "Plan",
                "value": ";;eh-plan",
                "inline": True},
                {"name": "Archetype",
                "value": ";;eh-archetype",
                "inline": True},
                {"name": "Profession",
                "value": ";;eh-profession",
                "inline": True},
                {"name": "Background",
                "value": ";;eh-background",
                "inline": True},
                {"name": "Feat",
                "value": ";;eh-feat",
                "inline": True},
                {"name": "Equipment",
                "value": ";;eh-equipment",
                "inline": True},
                {"name": "Companion",
                "value": ";;eh-companion",
                "inline": True},
                {"name": "Rule",
                "value": ";;eh-rule",
                "inline": True},
            ],
        }
        embed = embed_builder(help_data)
        await ctx.send(embed=embed)

    @commands.command(name="4e-help")
    async def foure_help(self, ctx):
        help_data = {
            "title": "D&D 4e Help Bot",
            "fields": [
                {"name": "Glossary",
                "value": ";;glossary",
                "inline": True},
                {"name": "Race",
                "value": ";;race",
                "inline": True},
                {"name": "background",
                "value": ";;background",
                "inline": True},
                {"name": "Theme",
                "value": ";;theme",
                "inline": True},
                {"name": "Class",
                "value": ";;class",
                "inline": True},
                {"name": "Paragon Path",
                "value": ";;paragon",
                "inline": True},
                {"name": "Epic Destiny",
                "value": ";;epic",
                "inline": True},
                {"name": "Power",
                "value": ";;power",
                "inline": True},
                {"name": "Feat",
                "value": ";;feat",
                "inline": True},
                {"name": "Ritual",
                "value": ";;ritual",
                "inline": True},
                {"name": "Weapon",
                "value": ";;weapon",
                "inline": True},
                {"name": "Implement",
                "value": ";;implement",
                "inline": True},
                {"name": "Armor",
                "value": ";;armor",
                "inline": True},
                {"name": "Companion",
                "value": ";;companion",
                "inline": True},
                {"name": "Deity",
                "value": ";;deity",
                "inline": True},
                {"name": "Poison",
                "value": ";;poison",
                "inline": True},
                {"name": "Disease",
                "value": ";;disease",
                "inline": True},
                {"name": "Monster",
                "value": ";;monster",
                "inline": True},
                {"name": "Trap",
                "value": ";;trap",
                "inline": True},
            ],
        }
        embed = embed_builder(help_data)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        help_data = {
            "title": "🍄 Help! *Wander*-ing what to do?",
            "description": "*No worries! Here's what I can do...*\n\n**Quirky Utilities:**\n- Dice: `;;r XdY` or `[[XdY]]` \n- Spoilered Dice: `;;||r XdY ||` or `[[||XdY ||]]`\n- Ping: Pong?\n\n**Compendium:**\n- D&D 4e: `;;4e-help`",
            "footer": {
                "text": "... just don't tell Minstrel anything!!"
            }
        }
        embed = embed_builder(help_data)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Utils(client))