import discord
import os

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
        # There are many more parameters for the embed constructor
        # you can experiment with:
        embed = discord.Embed(title="Pong", 
                              description="Description",
                              timestamp=message.created_at,
                              fields=[
                                  discord.EmbedField("Field Title 1", "Embed Description 1"),
                                  discord.EmbedField("Field Title 2", "Embed Description 2")
                              ])
        
        # You can pass the embed into message.channel.send or message.reply
        await message.reply(embed=embed)

bot.run(os.getenv('COMPBOT_TOKEN'))