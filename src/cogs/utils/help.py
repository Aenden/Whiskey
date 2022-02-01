from difflib import get_close_matches
from discord.ext import commands
from constants import COLOR
import discord

class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__(
            command_attrs={
                "help": "Shows help about the bot, a command, or a category",
            },
            verify_checks=False,
        )

    async def send_bot_help(self, mapping):
      ctx = self.context
      cats = []

      for cog, cmds in mapping.items():
        if cog and await self.filter_commands(cmds, sort=True):
          cats.append(cog)

      embed = discord.Embed(color=discord.Color(COLOR))
      for idx in cats:
        embed.add_field(
          inline=False,
          name=idx.qualified_name.title(),
          value=", ".join(map(lambda x: f"`{x}`", filter(lambda x: not x.hidden, idx.get_commands()))),
            )

        embed.set_footer(text="made with 💖 by Aendon")
        await ctx.send(embed=embed)

    async def send_command_help(self, command):
      embed = self.common_command_formatting(command)
      await self.context.send(embed=embed)
