import asyncio
import os
import numpy as np
import collections
import discord
import discord.opus
import opuslib
from faster_whisper import WhisperModel
from mcrcon import MCRcon
from discord.ext import commands
import discord.ext.voice_recv as voice_recv

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RCON_HOST = os.getenv('RCON_HOST', '127.0.0.1')
RCON_PORT = int(os.getenv('RCON_PORT', 25575))
RCON_PASSWORD = os.getenv('RCON_PASSWORD')

MODEL_SIZE = "base"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"

MOBS = ["zombie", "skeleton", "creeper", "spider", "enderman", "pig", "cow", "sheep", "chicken", "iron_golem", "villager", "wolf", "cat", "horse", "witch", "slime"]

print(f"Loading Whisper model ({MODEL_SIZE})...")
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

class MinecraftVoiceSink(voice_recv.AudioSink):
    def __init__(self, rcon, bot):
        self.rcon = rcon
        self.bot = bot
        # implementation omitted for brevity

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("You are not in a voice channel.")
        return
        
    channel = ctx.author.voice.channel
    vc = await channel.connect(cls=voice_recv.VoiceRecvClient)
    
    try:
        rcon = MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT)
        rcon.connect()
        print("✅ Connected to Minecraft RCON")
    except (ConnectionRefusedError, TimeoutError) as rcon_err:
        await ctx.send(f"Failed to connect to Minecraft: {rcon_err}")
        await vc.disconnect()
        return

    sink = MinecraftVoiceSink(rcon, bot)
    vc.listen(sink)
    
    await ctx.send(f"Connected to {channel.name} and Minecraft. Listening...")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected.")
    else:
        await ctx.send("I'm not in a voice channel.")

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    print("Commands: !join, !leave")

if __name__ == "__main__":
    if not DISCORD_TOKEN or not RCON_PASSWORD:
        print("Error: DISCORD_TOKEN and RCON_PASSWORD must be set in the environment.")
        exit(1)
        
    bot.run(DISCORD_TOKEN)