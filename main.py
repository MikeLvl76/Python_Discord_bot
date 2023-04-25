from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime
import discord, os, json

load_dotenv()

TOKEN: str = os.getenv('TOKEN')
GUILD: int = int(os.getenv('GUILD_ID'))
MAIN_CHANNEL: int = int(os.getenv('MAIN_CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    await bot.get_channel(MAIN_CHANNEL).send('THE BOT OF ALL TIME IS HERE!')

@bot.event
async def on_message(message: discord.Message):
    if not message.author.bot:
        print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

@bot.command(name="palindrome")
async def is_palindrome(ctx: commands.Context, *args):
    if len(args) == 0:
        ctx.reply('Provide one or many words.')
    res = {arg: 'Yes' if arg == arg[::-1] else 'No' for arg in args }
    await ctx.send(json.dumps(res, indent=4))

@bot.command(name='sub_sequence_frequency')
async def most_frequent_sub_sequence(ctx: commands.Context, arg: str, count: int):

    if arg == '':
        return await ctx.reply('Is this funny ? The sequence is empty.')   

    if count >= len(arg):
        return await ctx.reply('The subsequence must have lower size than the sequence.')
    
    if count == 0:
        return await ctx.reply('What\'s the point of doing this?')

    res = {}

    for i in range(len(arg) - (count - 1)):
        sub: str = arg[i:i+count]
        freq: int = res.get(sub) or 0
        res[sub]: int = freq + 1

    most_frequent_name: str = ''
    most_frequent_value: int = 0

    for item in res.items():
        if item[1] > most_frequent_value:
            most_frequent_name, most_frequent_value = item

    await ctx.send(json.dumps({ most_frequent_name: most_frequent_value }, indent=4))

@bot.command(name="max")
async def get_max(ctx: commands.Context, *args):

    if len(args) == 0:
        return ctx.reply('Provide at least one number')
    
    array = list(map(int, args))

    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    
    await ctx.send(f'Max in the list : {max}')

@bot.command(name="min")
async def get_min(ctx: commands.Context, *args):

    if len(args) == 0:
        return ctx.reply('Provide at least one number')
    
    array = list(map(int, args))

    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    
    await ctx.send(f'Max in the list : {min}')

@bot.command(name="date")
async def give_date(ctx: commands.Context):
    now = datetime.now()
    today = list(map(str, [now.day, now.month, now.year]))
    await ctx.send(f'Today date is {"-".join(today)}')

@bot.command(name="time")
async def give_time(ctx: commands.Context):
    now = datetime.now()
    time = list(map(str, [now.hour, now.minute, now.second]))
    await ctx.send(f'Today hour is {":".join(time)}')

bot.run(TOKEN)