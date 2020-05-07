import discord
from discord.ext  import commands
import time
import asyncio

class  help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def help(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed = discord.Embed(title="Commands:", description="Need commands? Here you go!   ",)
        embed.add_field(name='.help_mod', value='commands for mod', inline=False)
        embed.add_field(name=".ping", value="Shows Bot Latency", inline=False)
        embed.add_field(name=".ask", value="ask bot a question", inline=False)
        embed.add_field(name=".userinfo", value="Gets info about the user.", inline=False)
        embed.add_field(name=".av", value="shows avatar", inline=False)
        embed.add_field(name=".notfine", value="Why are we still here? Just to suffer?", inline=False)
        embed.add_field(name=".waj", value="Try it , It's An Order! ", inline=False)
        embed.add_field(name=".help", value="Brings you Here!", inline=False)
        await ctx.send(author.mention, embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def help_mod(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.add_field(name='.clear **n**', value='clear messages **n=number** ', inline=False)
        embed.add_field(name='.ban @member reason', value='ban a member', inline=False)
        embed.add_field(name='.kick @member reason', value='kick a member', inline=False)
        embed.add_field(name='.mute @member nd nh nm ns', value='mute member for a period of time ( ** nd= number of days,etc)', inline=False)

        
        await ctx.send(author.mention, embed=embed)

    



    



def setup(bot):
    bot.add_cog(help(bot))








        