#library's are down here ~~~~~~~~~~~~

import discord
import random
from discord.ext import commands

#variable's are down here ~~~~~~~~~~~~

client = commands.Bot(command_prefix = '.')

#client events are down here ~~~~~~~~~~~~~~

@client.event
async def on_ready():
await client.change_presence(status=discord.Status.idle, activity=discord.Game('.help you
goofy ass'))
print("bot is ready")

@client.event
async def on_member_join(member):
print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
print(f'{member} has left the server.')

@client.event
async def on_message_edit(before, after):
print('it works chief')

#client commands are down here ~~~~~~~~~~~~~~

@client.command()
async def ping(ctx):
await ctx.send(f'Pong! nigga {round(client.latency * 1000)}ms
<:FeelsBeatsMan:597591202614738947>')

@client.command()
async def heat(ctx):
await ctx.send('https://imgur.com/VvDgKDQ')

@client.command()
async def ofline(ctx):
await ctx.send('time to sleep')

@client.command()
async def spam_blind(ctx):
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('<@199099098895351808>')
await ctx.send('ITS TIME TO WAKE UP BLIND')

@client.command()
async def spam_epicwizard(ctx):
await ctx.send('dont try to spam epicwizard or i will blow up your minecraft house')

@client.command()
async def clown(ctx):
await ctx.send('https://imgur.com/BQ3us3b')

@client.command()
async def octane(ctx):
await ctx.send('https://imgur.com/YdU11gg')

@client.command()
async def send_boop(ctx, user):
server = client.get_guild(611335502947155968)
user = server.get_member_named(user)
await ctx.send('I booped the kid')
await user.send("boop")

@client.command()
async def yesorno(ctx):
await ctx.send('Discord, yes or no?')
response = client.wait_for_message(author=ctx.message.author, timeout=30)
if response.clean_content.lower() == 'yes':
await client.say('You said yes.')
elif response.clean_content.lower() == 'no':
await client.say('You said no.')
else:
await client.say("That isn't a valid response.")

#secret client code is down here ~~~~~~~~

client.run('NjExOTQ3NzM3NTU4Mjg2Mzky.XVe_OA.zN5rDUgdn6Sc4MyoGQCuuft4ZlI')
