import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import bot
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

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello (interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")
    ephemeral=True

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say (interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

if __name__ == '__main__':
        bot.run_discord_bot()

bot.run(TOKEN)