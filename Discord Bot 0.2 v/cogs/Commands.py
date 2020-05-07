import discord
from discord.ext  import commands

class  command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    client = commands.Bot(command_prefix ='.')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        if message.content.lower() == 'tea':
            await message.channel.send('Drink And Pee!')
        if message.content.lower() == 'Tea':
            await message.channel.send('Drink And Pee!')
        if message.content.lower() == 'TEA':
            await message.channel.send('Drink And Pee!')
        if message.content.lower() == '69':
            await message.channel.send('lmao')
        if message.content.lower() == 'F' :
            await message.channel.send('F')
        if message.content.lower() == 'f' :
            await message.channel.send('f') 
        if message.content.startswith('GG'):
            await message.channel.send('WP')        
        if message.content.startswith('gg'):
            await message.channel.send('wp')
        
                               
       


    @commands.Cog.listener("on_message")
    async def swear_listener(self, message:discord.Message):
        """Looks for swearing in the message and tells people off"""

        if message.author.bot:
            return

        content = set(message.content.lower().strip().split())
        swears = {"kys"}
        if content.intersection(swears): 
            await message.channel.send(f'That was very rude{message.author.mention} . Instead ,Take Your Own Advice!   ')
            
                
            

    @commands.command()
    async def notfine(self,message):
            embed = discord.Embed()
            notfine = embed.set_image(url='https://cdn.discordapp.com/attachments/342216929982808066/347541935990374400/not_fine.gif')
            await message.channel.send(embed=notfine)

    @commands.command()
    async def waj(self,message):
            embed = discord.Embed()
            waj = embed.set_image(url='https://b.top4top.io/p_1588r9fsl1.jpg')
            await message.channel.send(embed=waj)  

                

def setup(bot):
    bot.add_cog(command(bot))






















