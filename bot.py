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

@bot.command()
async def bot(ctx):
    try:
        await ctx.author.send("https://captchabynk6z.onrender.com")
        await ctx.message.add_reaction("✅")
    except discord.Forbidden:
        await ctx.send("Je n’ai pas pu t’envoyer de DM. Vérifie que tu les acceptes depuis ce serveur.")

# Lance le bot
bot.run(TOKEN)
