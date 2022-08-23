#Default start for a Discord.py bot project by jjkay03

import discord
from discord.ext import commands
from discord.ext.commands import check

#Bot prefix
client = commands.Bot(command_prefix = ".")
#Bot token will be read from "TOKEN.txt"
TOKEN = open("TOKEN.txt", "r").read()

#on_ready
@client.event
async def on_ready():
	#Bot activity status
	activity = discord.Game(name="Exemple bot", type=3)
	await client.change_presence(status=discord.Status.idle, activity=activity)
	
	print(">> BOT IS RUNNING")
	print(">> Name: {}".format(client.user.name))
	print(">> ID: {}".format(client.user.id))

	
#COMMAND: ping
@client.command(aliases=["Ping","PING", "p", "P"], help="Shows you the ping of the Bot")
async def ping(ctx):
	ping = round(client.latency * 1000)
	await ctx.send(f"**{ping}ms**")


#Client Run
client.run(TOKEN)