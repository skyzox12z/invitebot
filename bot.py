import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charge les variables d’environnement du fichier .env
load_dotenv()

# Récupère le token depuis la variable d’environnement
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté.")

@bot.command(name="botdm")
async def send_dm(ctx):
    if isinstance(ctx.channel, discord.TextChannel):  # Vérifie si la commande est envoyée dans un salon
        if ctx.channel.name != "cmds":
            await ctx.send("❌ This command only work in `#cmds`.")
            return

    try:
        await ctx.author.send("https://captchabynk6z.onrender.com/")
        await ctx.message.add_reaction("✅")
    except discord.Forbidden:
        await ctx.send("⚠️ I couldn't send you a dm. Check that you accept dm from this server.")

# Lance le bot
bot.run(TOKEN)

