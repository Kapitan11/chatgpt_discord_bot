# The load_dotenv function reads the key-value pairs from a .env file and sets them as environment variables.
from dotenv import load_dotenv
# The discord module is used to interact with the Discord API.
import discord
# The os module provides a way of using operating system dependent functionality.
import os
# Importing the chatgpt_response function from the app.chatgpt.openai module.
from app.chatgpt.openai import chatgpt_response

# Load environment variables from .env file.
load_dotenv()

# Get Discord bot token from the environment variables.
discord_token = os.getenv("DISCORD_TOKEN")

# Defining the MyClient class which extends the discord.Client class.
class MyClient(discord.Client):

    # The on_ready event is called when the bot has successfully logged in.
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    # The on_message event is called whenever a message is sent in a channel that the bot can see.
    async def on_message(self, message):
        print(message.content)

        # Ignore messages sent by the bot itself.
        if message.author == self.user:
            return

        # Check if the message starts with a valid command.
        command, user_message = None, None
        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
                break

        # If the message starts with a valid command, get a response from the GPT model and send it back to the channel.
        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt = user_message)
            await message.channel.send(f'Answer: {bot_response}')

# Create a new client instance with default intents and enable message content intents.
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
