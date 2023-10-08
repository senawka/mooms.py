#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio

async def start_bot():
    bot = commands.Bot(command_prefix='m!', intents=discord.Intents.all(), help_command=None)
    bot.load_extension('cogs.avatar_cog')

    @bot.event
    async def on_ready():
        server_count = len(bot.guilds)
        cog_count = len(bot.cogs)
        print(f'Bot is running. Connected to {server_count} server(s). Loaded {cog_count} cog(s).')

    return bot

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    bot = loop.run_until_complete(start_bot())

    with open('token.txt') as t:
        token = t.read()
    bot.run(token)