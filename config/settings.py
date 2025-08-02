import os
from dotenv import load_dotenv

load_dotenv()

# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_PREFIX = os.getenv("DISCORD_PREFIX")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")