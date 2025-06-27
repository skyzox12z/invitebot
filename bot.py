import discord
from discord.ext import commands
import os

# Récupère le token depuis Render
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

class CaptchaButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        url = "https://captchabynk6z.onrender.com/"
        self.add_item(discord.ui.Button(label="🔒 Verify Here", url=url))

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté.")

@bot.command(name="botdm")
async def send_dm(ctx):
    if isinstance(ctx.channel, discord.TextChannel):
        if ctx.channel.name != "cmds":
            await ctx.send("❌ This command only works in `#cmds`.")
            return

    try:
        view = CaptchaButtonView()
        await ctx.author.send("Click the button below to verify:", view=view)
        await ctx.message.add_reaction("✅")
        await ctx.send("✅ Check your DMs!")
    except discord.Forbidden:
        await ctx.send("⚠️ I couldn't send you a DM. Check if you accept DMs from the server.")

# Démarre le bot
bot.run(TOKEN)
