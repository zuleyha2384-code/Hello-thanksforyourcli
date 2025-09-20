import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! i {bot.user}, How can i help you?')

@bot.command()
async def suki(ctx, count_suki = 100):
    await ctx.send("suki" * count_suki)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def whats_up(ctx, count_whats_up = 1):
    await ctx.send("whats_up" * count_whats_up)






bot.run("MTQxNjQ4NjY2ODI3MzMyNDA3NA.Gpuqce.vIoCjsxMM4-qzieGVtfUT_N_uFWGCcHRxJrhxw")
