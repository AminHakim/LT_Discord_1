import discord
import emoji
from discord.ui import Select, View
from discord.ext import commands
from dotenv import load_dotenv
import os

print(f"Importing .env configuration...")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
RANGE1 = os.getenv('RANGE1')
RANGE2 = os.getenv('RANGE2')

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

bot = commands.Bot(command_prefix="-", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.command()
async def general(ctx):
    select = Select(min_values=1, max_values=4, placeholder="Please Choose 👇", options=[
        discord.SelectOption(label="Basic Info", value="Here is your basic infos!", emoji="ℹ", description="Staff's Basic Info"),
        discord.SelectOption(label="Total Work", value="Here is your total work list!", emoji="💼", description="Staff's Total Work List"),
        discord.SelectOption(label="Ongoing Work", value="Here is your ongoing work list!", emoji="⏲", description="Staff's Ongoing Work List"),
        discord.SelectOption(label="Finished Work", value="Here is your finished work list!", emoji="✅", description="Staff's Finished Work List"),
    ])

    async def my_callback(interaction):
        if select.values[0] == "Here is your basic infos!":
            print("Here is your basic infos!")
        if select.values[0] == "Here is your total work list!":
            print("Here is your total work list!")
        if select.values[0] == "Here is your ongoing work list!":
            print("Here is your ongoing work list!")
        if select.values[0] == "Here is your finished work list!":
            print("Here is your finished work list!")
        await interaction.response.send_message(f"➡:{select.values}")

    select.callback = my_callback
    view= View()
    view.add_item(select)

    await ctx.send("General Info", view=view)

bot.run(TOKEN)