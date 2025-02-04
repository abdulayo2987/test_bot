import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")


@bot.command()
async def welcome(ctx, member: discord.Member):
    # Step 1: Fetch user's avatar


    # Step 6: Send image in Discord
    await ctx.send(file=discord.File(output_path))


# Run your bot
bot.run("YOUR_BOT_TOKEN")
