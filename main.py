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

@bot.event
async def on_ready():
    print(f'Bot is online! Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Command 1: A simple ping/pong health check
@bot.tree.command(name="ping", description="Replies with Pong and the bot's latency!")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! Latency is {latency}ms.")

# Command 2: An interactive echo command that takes user input
@bot.tree.command(name="echo", description="The bot will repeat exactly what you say.")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"You said: {message}")

if __name__ == '__main__':
    bot.run(TOKEN)
