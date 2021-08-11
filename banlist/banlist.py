import discord
import asyncio
from discord.ext import commands

class Banlist(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

#------------------------------------------
# BANLIST
#
  @commands.command(name='banlist')
  async def banlist(self, ctx):
    banned_ids = []
    formatted_banlist = []
    banlist = await ctx.guild.bans()
    for banEntry in banlist:
      if not banEntry.user.id in banned_ids:
        formatted_ban = banEntry.user.name + "#" + str(banEntry.user.discriminator) + " : `" + str(banEntry.user.id) + "`"
        formatted_banlist.append(formatted_ban)
        banned_ids.append(banEntry.user.id)
    
    send_char_count = 0
    send_list = []
    for ban in formatted_banlist:
      send_char_count += len(ban)
      if send_char_count < 1500:
        send_list.append(ban)
      else:
        embed = discord.Embed(color=1, description="\n".join(send_list))
        print(len("".join(send_list)))
        await asyncio.sleep(1)
        await ctx.send(embed=embed)
        
        send_char_count = 0
        send_list = []
        send_char_count += len(ban)
        send_list.append(ban)
    embed = discord.Embed(color=1, description="\n".join(send_list))
    await ctx.send(embed=embed)
    print(formatted_banlist) 
#------------------------------------------
def setup(bot):
  bot.add_cog(Banlist(bot))
