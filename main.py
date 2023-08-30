
import nextcord
import os
import openai
import asyncio
from nextcord.ext import commands


intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)

openai.api_key = ""
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=nextcord.Game(name="/ask"))


@bot.slash_command(name='ask', description="used for chatting with the bot")
async def on_message(interaction: nextcord.Interaction, text):
    print(f'Message from {interaction.user}: {text}')
    if bot.user != interaction.user:
        channel = interaction.channel
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        messagetosend = response.choices[0].text
        await interaction.response.send_message(messagetosend)
        await interaction.response.defer()
        await interaction.followup.send(messagetosend)


    
bot.run("insert_token")


