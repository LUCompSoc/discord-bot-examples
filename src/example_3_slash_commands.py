import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# Here you can see we have a 'text' parameter as part of the function
# which will be part of the command on Discord.
@bot.slash_command(name="say", description="Make the bot say something.")
async def say_command(ctx: discord.ApplicationContext, text: str):

    # A slash command is considered an "interaction" rather than a message.
    # Every interaction needs to be responded to, and we can do it like this:

    await ctx.respond(text)

@bot.slash_command(name="private-message", description="The bot gives you a private message.")
async def say_command(ctx: discord.ApplicationContext):

    # Setting ephermal=True means the response will only be visible to the
    # person who used the command.

    await ctx.respond("This is a private message!", ephemeral=True)

@bot.slash_command(name="add", description="Adds two numbers.")
async def add_command(ctx: discord.ApplicationContext, num_1: int, num_2: int):
    res = num_1 + num_2
    await ctx.respond(str(res))

# Here, we're making a class which inherits discord.ui.View like this.
# This basically means we're creating a group of UI elements and their functionality.
class MessageWithButtonsView(discord.ui.View):
    @discord.ui.button(label="Button 1")
    async def button_1(self, button: discord.Button, interaction: discord.Interaction):
        await interaction.response.send_message("You pressed Button 1!")
    
    @discord.ui.button(label="Button 2")
    async def button_2(self, button: discord.Button, interaction: discord.Interaction):
        await interaction.response.send_message("You pressed Button 2!")

@bot.slash_command(name="button-example", description="Demo for buttons.")
async def say_command(ctx: discord.ApplicationContext):
    # By setting the 'view' parameter, we can pass in an instance of the MessageWithButtonsView
    # class we made before so that the response will contain the UI element specified within it.
    await ctx.respond("Here are some buttons you can press:", view=MessageWithButtonsView())

bot.run(os.getenv('COMPBOT_TOKEN'))