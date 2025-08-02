from discord.ext import commands
from config.settings import DISCORD_PREFIX, DISCORD_TOKEN

bot = commands.Bot(command_prefix=DISCORD_PREFIX, help_command=None, self_bot=True)

@bot.event
async def on_ready():
    print(f"[Logged in as {bot.user}]\nLatency: {bot.latency*1000}ms")
    await bot.load_extension("cogs.general")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)