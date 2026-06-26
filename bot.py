import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

KEYWORDS = [
    "ip",
    "ip?",
    "server ip",
    "player ip",
    "picklemc ip"
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower().strip() in KEYWORDS:

        embed = discord.Embed(
            title="🥒 PickleMC Server IP",
            color=0x57F287
        )

        embed.add_field(
            name="🟢 Java & Bedrock IP",
            value="```play.picklemc.fun```",
            inline=False
        )

        embed.add_field(
            name="🔌 Bedrock Port",
            value="```5831```",
            inline=False
        )

        embed.set_footer(text="Happy Survival! 💚")

        await message.reply(embed=embed, mention_author=False)

    await bot.process_commands(message)

bot.run(TOKEN)
