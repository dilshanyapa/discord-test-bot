#import packages
import discord
from discord.ext import commands 

#bot
client = commands.Bot(command_prefix="!",intents=discord.Intents.all())


#content
@client.event
async def on_ready():
    general =  client.get_channel(856436011827724298)
    await general.send("Hi My Friends Im Online")



@client.command(name = "server")
async def server(context):
    info = discord.Embed(
        title = "Hello",
        description = "This is a DILSHAN TECH Official Discord server",
        color = 0x00ff00
    )
    await context.message.channel.send(embed = info)
 

@client.command(name = "info")
async def info(context):
    maru = discord.Embed(
        title = "Owner",
        description = "Chanuka Dilshan Yapa",
        color = 0xFF1493

    )
    maru.add_field(name="MODERATOR",value="Sasandara Dilmina",inline=False)
    maru.add_field(name="ADMIN",value="Lahiru Lakshan",inline=False)
    maru.add_field(name="Released Date",value="05 jan 2021",inline=False)
    maru.set_image(url="https://cdn.discordapp.com/attachments/1057912832647233637/1059709663156912128/giphy.gif")
    maru.set_author(name="DILSHAN TECH")
    maru.set_footer(text="Thank You Have a Nice Day")
    
    await context.message.channel.send(embed = maru)

@client.command(name = "member")
async def member(context):
    kattiya = discord.Embed(
        title="Member Count",
        description="Owner 02 \nModerator 03 \nAdmin 01 \nFriends 06",
        color=0xFF4040
    )
    await context.message.channel.send(embed = kattiya)








@client.event
async def on_disconnect():
    general =  client.get_channel(856436011827724298)
    await general.send("Good Bye My Friends")


  




#run the bot
client.run("  tk")
