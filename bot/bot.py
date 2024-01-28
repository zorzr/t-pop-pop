import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
token = os.getenv('DISCORD_TOKEN')
if (len(token) < 1):
    print('Invalid token in env variables')
    exit(-1)

# Define bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='t!', intents=intents)


@bot.command(name='hello', pass_context=True)
async def hello(ctx):
    await ctx.send(f'Ciao {ctx.author.mention}!')

@bot.event
async def on_ready():
    print(f'Bot attivo: {bot.user.name}')


# Execute the bot
bot.run(token)
