import discord
import os

# This bot reads message content so we need to specify
# that as an intent here:
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message: discord.Message):
    # Make sure we won't be replying to ourselves.
    if message.author.id == bot.user.id:
        return

    if message.content.lower().startswith("ping"):
        await message.channel.send("Pong")

# Here we have an environment variable called DISCORD_TOKEN storing
# the token for the bot, you can replace this with something else
# but I'd recommend keeping it external not having it hard-coded:
bot.run(os.getenv('COMPBOT_TOKEN'))