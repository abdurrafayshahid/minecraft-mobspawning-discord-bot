# Voice-to-Mob Minecraft bot

A Discord bot that joins voice channels, transcribes speech with `faster-whisper`, and spawns mobs in Minecraft via RCON when it hears their names.

![Discord](https://img.shields.io/badge/Discord-Bot-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Minecraft](https://img.shields.io/badge/Minecraft-RCON-brightgreen)

## Features

- **Voice recognition**: Uses Whisper AI for speech-to-text.
- **Minecraft integration**: Spawns entities via RCON.
- **Fast processing**: Uses `faster-whisper` int8 quantization.
- **Configurable mobs**: Supports 16+ common Minecraft mobs.

## Prerequisites

- Python 3.8+
- Minecraft server with RCON enabled
- Discord bot token
- FFmpeg

### Minecraft server setup

Edit your `server.properties` file:

```properties
enable-rcon=true
rcon.port=25575
rcon.password=your_secure_password
broadcast-rcon-to-ops=false
```

To use GPU acceleration, install CUDA-enabled PyTorch and update `DEVICE = "cuda"` in `bot.py`.

## Troubleshooting

### Bot doesn't join voice channel

* Check if FFmpeg is installed and in your PATH.
* Verify the bot has "Connect" and "Speak" permissions.

### RCON connection fails

* Verify `enable-rcon=true` in `server.properties`.
* Check if your firewall allows the RCON port (default: 25575).
* Confirm the password matches exactly.

### Mob names not recognized

* Try saying the full mob name (e.g., "iron golem" not "golem").
* Check Discord microphone input levels.

## Dependencies

* [`discord.py`](https://github.com/Rapptz/discord.py)
* [`discord-ext-voice-recv`](https://www.google.com/search?q=https://github.com/ImayHaveBorked/discord-ext-voice-recv)
* [`faster-whisper`](https://github.com/guillaumekln/faster-whisper)
* [`mcrcon`](https://www.google.com/search?q=https://github.com/niccokunzmann/mcrcon)
* [`PyNaCl`](https://github.com/pyca/pynacl)
* [`torch`](https://pytorch.org/)

> [!IMPORTANT]
> Use strong passwords for RCON and never commit your `DISCORD_TOKEN` or `RCON_PASSWORD`. Restrict bot usage to trusted users.
