# To Do: add more banned words in the banned_words.json file.
# also add better response messages.
import discord
from discord.ext import commands
import random
import json
import os

class Keyword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_words = self.load_banned_words()
        self.response_messages = [
            "https://cdn.discordapp.com/attachments/1062092719343812699/1160671382850519120/MoomsSpeeeeen.gif"
        ]

    def load_banned_words(self):
        file_path = os.path.join('config', 'banned_words.json')
        with open(file_path, 'r') as file:
            banned_words_data = json.load(file)
        return banned_words_data.get("BannedWords", [])

    @commands.Cog.listener()
    async def on_message(self, message):
        if any(word in message.content for word in self.banned_words):
            await message.delete()
            await message.channel.send(random.choice(self.response_messages))

def setup(bot):
    bot.add_cog(Keyword(bot))