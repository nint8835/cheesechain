import discord
from discord import app_commands

from .config import config

guild = discord.Object(config.guild_id)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)


@client.event
async def on_ready() -> None:
    print("Bot ready, syncing commands")
    await tree.sync(guild=guild)


__all__ = ["guild", "client", "tree"]
