from discord.ext import commands

from config.settings import DISCORD_PREFIX, DISCORD_TOKEN

client = commands.Bot(command_prefix=DISCORD_PREFIX, help_command=None, self_bot=True)


@client.event
async def on_ready():
    print(f"[Logged in as {client.user}]\nLatency: {client.latency*1000}ms")
    await client.load_extension("cogs.general")
    await client.load_extension("cogs.chat")
    await client.load_extension("cogs.logger")


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
