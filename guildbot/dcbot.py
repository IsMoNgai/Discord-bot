import discord
from discord.ext import commands
from discord.utils import get
from keepalive import keep_alive
from guildlist import string


client = commands.Bot(command_prefix = '$', intents = discord.Intents().all())

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    channel = client.get_channel(619835797373321246)
    await channel.send(':partying_face:'f'{member.mention} welcome to Guild server **ULTRATRYHARDS GUILD** !')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(619835797373321246)
    await channel.send(':confused:'f'{member.mention} just left the Guild server!')

@client.command()
async def guildlist(ctx):
    guild = client.get_guild(619835797373321244)
    role = get(guild.roles, id=619836687937175586)
    memberlist = []
    for guild in client.guilds:
        for member in guild.members:
            if role in member.roles:
                if member.nick != None:
                    memberlist.append(member.nick)

    string = '```\n' + memberlist + '```'

    await ctx.send("Guild members (in this discord) in game name list:\n" + "treat - as _ if you want to invite this person in game!!!!\n" + "if you can't see your name here register your ign now!!\n")
    await ctx.send(string)

@client.command()
async def memberlist(ctx):
    memberlist = string.guildmemberlist()
    embed = discord.Embed(
        title = '>>ULTRATRYHARDS Guild Member List<<',
        description = memberlist,
        colour = 0xFFC300
    )
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(
    title = 'Welcome to ULTRATRYHARDS family:heart:',
    description = 'This guild is a BW guild but is ok that if u are active . \n'
    'the founder of this guild is ultra_timelord, if u have any question about this guild u can ask '
    'any staff of this guild, they will try their best to answer u:smiley: \n'
    'u can find guild members in the guild chat or party to play with u!!\n'
    'if u have any suggestion that want us to improve, tell us and let us know (@our name)\n'
    'Check out our guild information section for more informations!!\n'
    'BTW PLEASE FOLLOW THE RULES LISTED!!!!\n',
        colour = 0xFFC300
    )

    embed.set_footer(text='Hope u have a great day in this guild :)')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)

@client.command()
async def guildinfo(ctx):
    InfoList = string.getguildinfo()
    embed = discord.Embed(
    title = InfoList[0] + ' [' + InfoList[1] + ']',
    description = 'Created: ' + '```\n' + InfoList[2] + '```\n' + 'Members: ' + '```\n' + InfoList[3] + '/125' + '```\n' + 'Level: ' + '```\n' + InfoList[4] + '```\n' + 'Online Player: ' + '```\n' + InfoList[5] + '```\n',
        colour = 0xFFC300
    )

    embed.set_footer(text='Hope u have a great day in this guild :)')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)

@client.command()
async def register(ctx, newnick):
    member = ctx.message.author
    guild = ctx.message.author.guild
    role = discord.utils.get(guild.roles, id = 619836687937175586)
    await member.add_roles(role)
    await ctx.message.author.edit(nick = newnick)
    await ctx.send(ctx.message.author.mention + 'Register complete ! Thank you for verifying your username')

keep_alive()

client.run('ODgwNjg4NDYxODUyNjA2NDg0.YSh7Cw.3asBlFfRs2MW3qd0XQ_L71X-tLY')