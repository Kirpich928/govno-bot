import discord
from discord.ext import commands
from config import settings

client = commands.Bot(command_prefix = (settings['prefix']))

@client.event

async def on_ready():
		print('BOT connected!')

@client.command()
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

	await member.add_roles(mute_role)
	await ctx.send('{0} получает мут за нарушение прав!'.format(member.mention))

@client.command()
@commands.has_permissions(administrator = True)

async def unmute(ctx, member: discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

	await member.remove_roles(mute_role)
	await ctx.send('{0} теперь снова может писать в чат!'.format(member.mention))

#RUN

client.run(str(token))
