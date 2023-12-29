import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def verify(ctx):
    """Initiate the verification process."""
    verification_message = await ctx.send("React with ✅ to verify yourself.")
    await verification_message.add_reaction("✅")

@bot.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        channel = reaction.message.channel
        if str(reaction.emoji) == "✅" and channel.name == "verification":
            verified_role = discord.utils.get(user.guild.roles, name="Verified")
            await user.add_roles(verified_role)
            await channel.send(f"{user.mention} has been verified!")

bot.run('MTE5MDM4NjA0MTg3MDM1MjQ3NA.GWR3IJ.qGwYsdmpPbRMFxzohA1c7favDckVZRUo71-f2o')
