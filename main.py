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

@bot.command(name='sub_sequence_frequency')
async def most_frequent_sub_sequence(ctx: commands.Context, arg: str, count: str):

    if arg == '':
        return await ctx.reply('Is this funny ? The sequence is empty.')

    size = int(count)    

    if size >= len(arg):
        return await ctx.reply('The subsequence must have lower size than the sequence.')
    
    if size == 0:
        return await ctx.reply('What\'s the point of doing this?')

    res = {}

    for i in range(len(arg) - (size - 1)):
        sub: str = arg[i:i+size]
        freq: int = res.get(sub) or 0
        res[sub]: int = freq + 1

    most_frequent_name: str = ''
    most_frequent_value: int = 0

    for item in res.items():
        if item[1] > most_frequent_value:
            most_frequent_name, most_frequent_value = item

    await ctx.send(json.dumps({ most_frequent_name: most_frequent_value }, indent=4))

bot.run(TOKEN)