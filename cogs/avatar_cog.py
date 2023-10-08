import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        if not user:
            user = ctx.author

        avatar_url = user.avatar_url_as(format='png')  # instead of .webp

        embed = discord.Embed(title=f"Avatar of {user}", color=discord.Color(0x000000))
        embed.set_image(url=avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))