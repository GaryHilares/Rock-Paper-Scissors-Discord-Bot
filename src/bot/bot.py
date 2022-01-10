from discord.ext import commands
from bot.commands import rock_paper_scissors

discord_client = commands.Bot(command_prefix="bot!")
discord_client.add_command(rock_paper_scissors)