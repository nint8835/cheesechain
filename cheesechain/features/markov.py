import json
import pathlib
from functools import lru_cache

import discord
import markovify
from discord import app_commands

from cheesechain.bot import guild, tree


@lru_cache
def get_markov_model(user_id: str, channel: str) -> markovify.Text:
    text = ""
    for file in (pathlib.Path("dataset") / channel).iterdir():
        if file.is_dir() or file.suffix != ".json":
            continue
        with open(file, encoding="utf8") as f:
            messages = json.load(f)

            for message in messages:
                if "text" not in message or "user" not in message:
                    continue
                if message["user"] != user_id:
                    continue

                text += message["text"] + "\n"

    return markovify.NewlineText(text, state_size=2)


@tree.command(guild=guild)
@app_commands.describe(
    user_id="Slack user ID of the user to generate a message for",
    channel="Name of the Slack channel to use as a dataset for message generation",
)
async def generate(
    interaction: discord.Interaction, user_id: str, channel: str
) -> None:
    model = get_markov_model(user_id, channel)

    sentence = model.make_short_sentence(1000)

    embed = discord.Embed()
    embed.colour = discord.Colour.blurple()
    embed.set_author(name=f"{user_id} - #{channel}")

    embed.description = sentence

    await interaction.response.send_message(embed=embed)
