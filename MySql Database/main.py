import mysql.connector
import discord
from discord.ext import commands

intents = discord.Intents().all()
prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
token = " "

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbtest'
)

cursor = mydb.cursor(dictionary=True)

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def set(ctx):
    sql = "INSERT INTO users (ID, BALANCE) VALUES (%s, %s)"
    val = (ctx.author.id, "50")
    cursor.execute(sql, val)

@bot.command()
async def bal(ctx):
    cursor.execute(f"SELECT JOBSCOPE from user where NAME = {ctx.author.id}")

    rows = cursor.fetchall()
    for row in rows:
        await ctx.send(row["JOBSCOPE"])



bot.run(token)