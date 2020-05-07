import discord
from discord.ext  import commands

class  bad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener("on_message")
    async def swear_listener(self, message:discord.Message):
        """Looks for swearing in the message and tells people off"""

        if message.author.bot:
            return

        content = set(message.content.lower().strip().split())
        swears = {"Nigga", "Nigger", "nigga", "nigger", "blacknigga", "blacknigger"}
        if content.intersection(swears):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            try:
                await message.channel.send(f"{message.author.mention}, **#Warned**.")
            except discord.Forbidden:
                pass



def setup(bot):
    bot.add_cog(bad(bot))
   
   
   
   



















   