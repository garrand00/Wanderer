import discord
from discord.ext import commands

from tools.data_helper import search_command_builder
from data.eh_data import archetype_data, class_data, background_data, plan_data, talent_data, feat_data, rule_data, profession_data, companion_data
from data.eh_embed_template import archetype_embed, class_embed, background_embed, profession_embed, plan_embed, talent_embed, feat_embed, rule_embed, companion_embed

class EverydayHeroes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("eh.py loaded.")

    @commands.command(name="eh-class")
    async def class_search(self, ctx, *, keyword: str):
        await search_command_builder(self, ctx, keyword, class_data, class_embed)
    
    @commands.command(name="eh-background", aliases=["eh-bg"])
    async def background(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, background_data, background_embed)
    
    @commands.command(name="eh-profession", aliases=["eh-prof"])
    async def profession(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, profession_data, profession_embed)

    @commands.command(name="eh-plan")
    async def plan(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, plan_data, plan_embed)

    @commands.command(name="eh-archetype")
    async def archetype(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, archetype_data, archetype_embed)
    
    @commands.command(name="eh-talent")
    async def talent(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, talent_data, talent_embed)
    
    @commands.command(name="eh-feat")
    async def feat(self, ctx, *, keyword:str):
        await search_command_builder(ctx, keyword, feat_data, feat_embed)
    
    
async def setup(client):
    await client.add_cog(EverydayHeroes(client))
