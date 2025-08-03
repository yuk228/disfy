import discord
from discord.ext import commands

from config.settings import DISCORD_CHANNEL_ID, DISCORD_PREFIX

class Chat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id != int(DISCORD_CHANNEL_ID):
            return
        if message.author.id != self.bot.user.id:
            return
        if not message.content.startswith(f"{DISCORD_PREFIX}chat"):
            return
        

async def setup(bot: commands.Bot):
    await bot.add_cog(Chat(bot))