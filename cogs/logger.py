import discord
from discord.ext import commands


class Logger(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        async for entry in message.guild.audit_logs(
            limit=1, action=discord.AuditLogAction.message_delete
        ):
            deleter = entry.user
        print(f"{deleter} deleted {message.content} in {message.channel.name}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Logger(bot))
