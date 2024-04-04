import discord
import asyncio

from discord.ext import commands

from data.foure_data import glossary_data, race_data, background_data, theme_data, class_data, paragon_data, epic_data, power_data, feat_data, ritual_data, item_data, weapon_data, implement_data, armor_data, deity_data, companion_data, poison_data, disease_data, monster_data, trap_data
from data.foure_embed_template import foure_embed

from tools.data_helper import search_command_builder

class FourthEdition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.errorMsg = "Something is wrong. Please check your input"

    @commands.Cog.listener()
    async def on_ready(self):
        print("foure.py loaded.")

    @commands.command(name="glossary")
    async def glossary_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, glossary_data, foure_embed)

    @commands.command(name="race")
    async def race_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, race_data, foure_embed)

    @commands.command(name="background")
    async def background_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, background_data, foure_embed)
    
    @commands.command(name="theme")
    async def theme_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, theme_data, foure_embed)

    @commands.command(name="class")
    async def class_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, class_data, foure_embed)

    @commands.command(name="paragon")
    async def paragon_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, paragon_data, foure_embed)

    @commands.command(name="epic")
    async def epic_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, epic_data, foure_embed)

    @commands.command(name="power")
    async def power_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, power_data, foure_embed)

    @commands.command(name="feat")
    async def feat_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, feat_data, foure_embed)
    
    @commands.command(name="ritual")
    async def ritual_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, ritual_data, foure_embed)

    @commands.command(name="item")
    async def item_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, item_data, foure_embed)

    @commands.command(name="weapon")
    async def weapon_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, weapon_data, foure_embed)

    @commands.command(name="implement")
    async def implement_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, implement_data, foure_embed)

    @commands.command(name="armor")
    async def armor_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, armor_data, foure_embed)
    
    @commands.command(name="companion")
    async def companion_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, companion_data, foure_embed)

    @commands.command(name="deity")
    async def deity_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, deity_data, foure_embed)

    @commands.command(name="poison")
    async def poison_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, poison_data, foure_embed)

    @commands.command(name="disease")
    async def disease_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, disease_data, foure_embed)

    @commands.command(name="monster")
    async def monster_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, monster_data, foure_embed)

    @commands.command(name="trap")
    async def trap_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, trap_data, foure_embed)
    
async def setup(client):
    await client.add_cog(FourthEdition(client))