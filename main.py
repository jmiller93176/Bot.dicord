import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the secret token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure basic intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot framework
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    # This hook runs immediately when the bot starts
    async def setup_hook(self):
        # Syncs the slash commands to Discord's servers
        await self.tree.sync()
        print("Slash commands synced to Discord!")

bot = MyBot()

