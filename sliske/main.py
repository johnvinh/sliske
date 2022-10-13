import discord
import json

with open('token.json', 'r') as f:
    token = json.load(f)["token"]

bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(guild_ids=[323973879288692746])
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

bot.run(token)
