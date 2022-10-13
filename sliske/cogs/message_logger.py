import discord
from discord.ext import commands


class MessageLogger(commands.Cog):
    bot: discord.Bot

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        logs_channel = self.bot.get_channel(606108509087465482)
        content = f"The user {message.author.name}#{message.author.discriminator} has deleted a message:\n```"
        content += message.content
        content += "\n```"
        await logs_channel.send(content)


def setup(bot: discord.Bot):
    bot.add_cog(MessageLogger(bot))
