# To Do: make images able to be included in the embed.
import discord
from discord.ext import commands
import random
import json
import os

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deleted_messages = {}
        self.no_deleted_messages = [
            "Looks like there are no deleted messages to snipe. Keep an eye out for juicy content!",
            "Sorry, nothing to snipe here.",
            "No deleted messages to snipe, but don't worry, there's always more drama waiting to happen!",
            "No deleted messages, no problem. Time to grab some popcorn and wait for the next snipe-worthy moment!",
            "No deleted messages detected. Looks like everyone's on their best behavior!",
            "No deleted messages found. Please stand by for further sniping opportunities.",
        ]

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.deleted_messages[message.channel.id] = message

    @commands.command()
    async def snipe(self, ctx):
        channel_id = ctx.channel.id

        if channel_id in self.deleted_messages:
            deleted_message = self.deleted_messages[channel_id]
            author = deleted_message.author
            content = deleted_message.content
            avatar_url = author.avatar_url
            timestamp = deleted_message.created_at

            embed = discord.Embed(color=discord.Color(0x000000))
            embed.set_author(name=author.name, icon_url=avatar_url)
            embed.timestamp = timestamp

            if deleted_message.attachments:
                attachment = deleted_message.attachments[0]
                if attachment.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    image_url = attachment.url
                    embed.description = f"**Deleted Message Sent:**\n[Sniped Image]({image_url})"
                    embed.set_image(url=image_url)
                else:
                    embed.description = f"**Deleted Message Sent:**\n{content}"
            else:
                embed.description = f"**Deleted Message Sent:**\n{content}"

            await ctx.send(embed=embed)
        else:
            with open(os.path.join('config', 'elevated_users.json'), 'r') as f:
                elevated_users_data = json.load(f)

            elevated_user_ids = [user["User ID"] for user in elevated_users_data.get("ElevatedUsers", [])]
            if str(ctx.author.id) in elevated_user_ids or ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_messages:
                message = random.choice(self.no_deleted_messages)
                await ctx.send(message)
            else:
                await ctx.send("You don't have permission to use this command.")

def setup(bot):
    bot.add_cog(Snipe(bot))

