import discord
from dotenv import load_dotenv
import os
load_dotenv() 

pub_key = os.getenv("PUBLIC_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()


# temp change
client.run(pub_key)
