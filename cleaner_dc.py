from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def clear(ctx, amount=None):
    if amount is None:
        await ctx.channel.purge(limit=10)
    elif amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=int(amount))

client.run(DISCORD TOKEN)