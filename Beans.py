from discord.ext import commands
import discord
from random import randrange

f = open("secret.txt", 'r')
BOT_TOKEN = f.read()
CHANNEL_ID = 1187269830076796959
SPAM_CHANNEL = 1275643495150784553
PERMISSIONS = 585809917103168

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot running!")
    channel = bot.get_channel(CHANNEL_ID)
    spam_channel = bot.get_channel(SPAM_CHANNEL)
    await spam_channel.send("Mighty beans online")

@bot.command()
async def beans(ctx, die, winner):
    roll = randrange(1, int(die))
    print(roll)
    await ctx.send(f"Rolling a d{die}")
    if roll == int(winner):
        await ctx.send(f"Rolled a {roll}, guess its a mighty beans night!🫘")
    else:
        await ctx.send(f"Rolled a {roll}, guess it isn't a mighty beans night 🥺")
@beans.error
async def beansError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command Usage: !beans {{die_size}} {{winning_number}}')
        
bot.run(BOT_TOKEN)
