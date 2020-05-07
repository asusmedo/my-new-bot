import discord
from discord.ext  import commands

class  error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
             await ctx.send("You Don't Have permission To Do That!")
        if isinstance(error, discord.ext.commands.CommandNotFound):
             await ctx.send('This Not A Command')
        if isinstance(error,discord.ext.commands.errors.MissingRequiredArgument):
             await ctx.send(' member is a required argument that is missing')

    
        

        raise error



def setup(bot):
    bot.add_cog(error(bot))