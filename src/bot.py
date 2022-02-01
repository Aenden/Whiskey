import discord
from discord.ext import commands
import jishaku
import config

class Whiskey(commands.Bot):
  def __init__(self, **kwags):
    super().__init__(
      command_prefix=commands.when_mentioned_or(">"),
      strip_after_prefix=True,
      case_insensitive=True,
      intents=discord.Intents.all(),
      activity=discord.Activity(type=discord.ActivityType.playing, name="Are you drunk?"),
        **kwargs,

    )

    self.load_extension("jishaku")

    async def on_ready(self):
      print("whiskey loaded")

    async def on_command_error(self, ctx, error):
      ignorable = (CommandNotFound,)
      if not isinstance(error, ignorable):
        return await ctx.send(error)


if __name__ == "__main__":
    Whiskey().run(config.DISCORD_TOKEN)
