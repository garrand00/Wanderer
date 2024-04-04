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
                {"name": "Class",
                "value": ";;eh-class",
                "inline": True},
            ],
        }
        embed = embed_builder(help_data)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Utils(client))