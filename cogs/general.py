import discord
from discord.ext import commands

from services.llm import generate_text_with_gemini

from colorama import Fore
from config.settings import DISCORD_PREFIX
import time

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context, command: str=None):
        if command:
            match command:
                case "purge":
                    await ctx.reply(f"```{DISCORD_PREFIX}purge [channel_id] [amount] [float(time)]\n{DISCORD_PREFIX}purge 1370064823085170698 100 1.45```", delete_after=5)
                    await ctx.message.delete(delay=5)
                case "gemini":
                    await ctx.reply(f"```{DISCORD_PREFIX}gemini [prompt]\n{DISCORD_PREFIX}gemini Hello World```", delete_after=5)
                    await ctx.message.delete(delay=5)
                case _:
                    await ctx.reply(f"Command not found: `{command}`", delete_after=5)
                    await ctx.message.delete(delay=5)
        else:
            await ctx.reply(f"```{DISCORD_PREFIX}help [command]\n{DISCORD_PREFIX}help purge```", delete_after=5)
            await ctx.message.delete(delay=5)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f"Pong! Latency: `{latency}ms`", delete_after=5)
        await ctx.message.delete(delay=5)

    @commands.command()
    async def purge(self, ctx: commands.Context, channel_id: int, amount: int, limit: float=1.45):
        count = 0
        channel = self.bot.get_channel(int(channel_id))
        if not channel:
            await ctx.reply(f"Channel not found: `{channel_id}`", delete_after=5)
            await ctx.message.delete(delay=5)
            return
        messages = [message async for message in channel.history(limit=amount + 1)]
        for msg in messages:
            if msg.author == self.bot.user:
                try:
                    await msg.delete()
                    count += 1
                    print(Fore.RED+"[DELETED]"+Fore.RESET+f" {msg.author} | {msg.content}")
                    time.sleep(float(limit))
                except discord.errors.Forbidden as e:
                    if e.code == 50021: 
                        amount += 1
                        pass
            else:
                amount += 1
        await ctx.reply(f"`deleted`", delete_after=5)
        await ctx.message.delete(delay=5)
        print(Fore.GREEN+"[FINISHED]"+Fore.RESET+f" Count: {count}")
    
    @commands.command()
    async def gemini(self, ctx: commands.Context, *, prompt: str="Hello World"):
        if len(prompt) > 1024:
            await ctx.reply("Prompt is too long", delete_after=5)
            await ctx.message.delete(delay=5)
            return
        
        response = await generate_text_with_gemini(prompt)
        
        chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
        for i, chunk in enumerate(chunks):
            if i == 0:
                await ctx.reply(f"Gemini-2.0-flash: {chunk}")
            else:
                await ctx.send(chunk)

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))