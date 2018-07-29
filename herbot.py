import discord
import json
import os
import asyncio
from discord.ext import commands


TOKEN = 'NDQ1OTg1MTU0NzcxNTgzMDA2.DfhEww.TWkGizTfREQz3krqVI8m06UOoBE'
client = commands.Bot(command_prefix = '.')
os.chdir(r"C:\Users\samhe\OneDrive\Sams Folder\Sams Folder\Discord\data")
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help'))
    print("Bot is ready. ")

@client.event
async def on_message(message):
    print("A user has sent a message.")
    await client.process_commands(message)

#ping command // Ping Pong!
@client.command()
async def ping():
    await client.say('Pong!')
    

#hello command // hello!
@client.command()
async def hello():
    await client.say('Hello! :wave:')
    

#echo command // Repeats after you!
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' ' 
    await client.say(output)
    

#clear command // delete messages
@client.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted. ')
    

#PPL Joining // 
client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name= "『Players』")
    await client.add_roles(member, role)

#doesnt work
client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(message, "Welcome to the Overt Community!")
    print("sent message to " + member.name)
    

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x0000ff)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)
    

@client.command(pass_context=True)
async def help():
    embed = discord.Embed(title="Help Menu", description="Here's what I could find.", color=0x0000ff)
    embed.add_field(name='.ping', value="Returns Pong!", inline=False)
    embed.add_field(name='hello', value="Friendly Chat Response!", inline=False)
    embed.add_field(name='.info @', value="Get information on anyone inside the server", inline=False)
    embed.add_field(name='.serverinfo', value="Info on Server", inline=False)
    embed.add_field(name='.echo', value="Repeats after you!", inline=False)
    embed.add_field(name='.join', value="Join Voice Channel", inline=False)
    embed.add_field(name='.leave', value="Leave Voice Channel", inline=False)
    embed.add_field(name='.clear x', value="Deletes x number of Messages - **10 LIMIT**", inline=False)
    await client.say(embed=embed)
    
   
@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x0000ff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
    
#Music Code //
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

#level system
@client.event
async def on_member_join(member):
    with open('users.json', "r") as f:
        users = json.load(f)


    await update_data(users, member)

    with open('users.json', "w") as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    with open('users.json', "r") as f:
        users = json.load(f)
    await client.process_commands(message)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', "w") as f:
        json.dump(users, f)

async def update_data(users , user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience']=0
        users[user.id]['level']=1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has levelled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
    



client.login(process.env.TOKEN):
    

