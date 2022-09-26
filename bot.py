import discord
from discord.ext import commands
import asyncio
import secret

intents = discord.Intents.all()
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print('{0.user} is ready to use'.format(bot))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    print(message.content)
    await bot.process_commands(message)    

@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await context.send("Not enough arguments for command")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(secret.TOKEN)