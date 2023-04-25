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

def get_max(*args):

    if len(args) == 0:
        return 0
    
    array = list(map(int, args))

    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]

    return max

def get_min(*args):

    if len(args) == 0:
        return 0
    
    array = list(map(int, args))

    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    
    return min

@bot.command(name="max")
async def max_in_list(ctx: commands.Context, *args):
    max = get_max(args)
    await ctx.send(f'Max in the list : {max}')

@bot.command(name="min")
async def min_in_list(ctx: commands.Context, *args):
    min = get_min(args)
    await ctx.send(f'Max in the list : {min}')

@bot.command(name="sort_descending")
async def sort_list_descending(ctx: commands.Context, *args):

    if len(args) == 0:
        return ctx.reply('Provide at least one number')
    
    array = list(map(int, args))

    for k in range(len(array)):
        max = get_max(*array[k:])
        if array[k] < max:
            index = array.index(max)
            array[k], array[index] = max, array[k]
            
    await ctx.send(f'Sorted list : {array}')

@bot.command(name="sort_ascending")
async def sort_list_ascending(ctx: commands.Context, *args):

    if len(args) == 0:
        return ctx.reply('Provide at least one number')
    
    array = list(map(int, args))

    for k in range(len(array)):
        min = get_min(*array[k:])
        if array[k] > min:
            index = array.index(min)
            array[k], array[index] = min, array[k]
            
    await ctx.send(f'Sorted list : {array}')

@bot.command(name="bubble_sort")
async def do_bubble_sort(ctx: commands.Context, *args):

    if len(args) == 0:
        return ctx.reply('Provide at least one number')
    
    array = list(map(int, args))

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    await ctx.send(f'Sorted list : {array}')

@bot.command(name='count_occurrences')
async def count_occurences(ctx: commands.Context, arg: str):
    if arg == '':
        return await ctx.reply('Provide a word')
    
    res = {}

    for char in arg:
        freq: int = res.get(char) or 0
        res[char]: int = freq + 1

    await ctx.send(json.dumps(res, indent=4))

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