from RPY import GetPosts
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def getposts(ctx,limit,tags,pn):
    for i in GetPosts(limit,tags,pn):
        await ctx.send(i)

bot.run('token')