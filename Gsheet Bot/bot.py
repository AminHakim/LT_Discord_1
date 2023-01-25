print(f"Starting bot...")


import time
startTime = time.time()


print(f"Importing modules...")


import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


print(f"Importing .env configuration...")



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

load_dotenv()
TOKEN = 'MTA2MjkwMjE2NzA4Nzg3NDA3OA.GdUV1R.I7KGyUu8-wkR5tKAsiUpemDLOlEypZzSbvbp08'
SAMPLE_SPREADSHEET_ID = '1sNv7X_7Zy-8hEvafrs1E7-wpmgSmmzt0vYBe2Ywcqn8'
SAMPLE_RANGE1 = 'Sheet1!A1:B'
SAMPLE_RANGE2 = 'Sheet1!C1:D'


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=discord.Intents.all(), command_prefix= "!")

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")


print("Initializing Google Authentication...")



creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


print(f"Startup complete!\t[ {(time.time()-startTime):.2f}s ]")



@bot.command(name='test')
async def testCommand(ctx, *args):
    if (len(args) == 0):
        await ctx.send("Please send some arguments!")
    else:
        valuesToWrite = [
            [ "C1","D1" ],
            [ "C2","D2" ],
            [ "C3","D3" ],
        ]
        body = {
            'values': valuesToWrite
        }
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE1).execute()
        result2 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE2, valueInputOption='USER_ENTERED', body=body).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s' % (row[0], row[1]))
                await ctx.send(f"{row[0]} {row[1]}")
        print(f"Arg0: {args[0]}")




bot.run(TOKEN)