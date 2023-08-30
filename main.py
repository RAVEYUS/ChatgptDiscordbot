appid = 1128620285713715270
#public_key=cc2477dd93ef32fc5f870feb50f918ab1a0a76850222e75fc619622d868c4026
import nextcord
import os
import openai
import asyncio
from nextcord.ext import commands

token="MTEyODYyMDI4NTcxMzcxNTI3MA.GCsVL4.qPJTabzzEo3LdFob4kT6PNoB3WVP6jY_c91qIc"
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)

openai.api_key = "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"
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


