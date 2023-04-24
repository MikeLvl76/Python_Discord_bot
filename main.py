import json
import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.getenv('TOKEN')
GUILD: int = int(os.getenv('GUILD_ID'))
MAIN_CHANNEL: int = int(os.getenv('MAIN_CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    await bot.get_channel(MAIN_CHANNEL).send('THE BOT OF ALL TIME IS HERE!')

@bot.event
async def on_message(message: discord.Message):
    if not message.author.bot:
        print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

@bot.command()
async def palindrome(ctx: commands.Context, *args):
    if len(args) == 0:
        ctx.reply('Provide one or many words.')
    res = {arg: 'Yes' if arg == arg[::-1] else 'No' for arg in args }
    await ctx.send(json.dumps(res, indent=4))

bot.run(TOKEN)