import discord
from discord.ext import commands
import time
import random
class Mod(commands.Cog):
    """Decancer, dehoist and other mod commands"""
    def __init__(self, bot):
      self.bot=bot
    @commands.command(description="[Mass]Ban The Given Member(s)", help="ban <member(s)> [--reason <reason>]", aliases=["massban"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx):
      try:
        ctx.message.mentions[0]
      except:
        await ctx.send("Mention atleast 1 member!")
      else:
        banned=[]
        failed=[]
        if "--reason" not in ctx.message.content:
          reason="Massban"
        else:
          reason=ctx.message.content.split("--reason")
          reason=reason[1]
        for member in ctx.message.mentions:
          try:
            await member.ban(reason=reason)
            banned.append(f"`{member}`")
          except:
            failed.append(f"`{member}`")
        if banned==[]:
          await ctx.send("Failed to ban any member")
        else:
          texttosend="\n".join(banned)
          embed=discord.Embed(title=f"Banned {len(banned)} Member(s)",description=texttosend,color=0x00FF00)
          await ctx.send(embed=embed)
          embed.add_field(name="Reason",value=reason,inline=False)
        if failed==[]:
          await ctx.send("Banned all members")
        else:
          texttosend="\n".join(failed)
          embed=discord.Embed(title=f"Failed To Ban {len(failed)} Member(s)",description=texttosend,color=0xFF0000)
          await ctx.send(embed=embed)      
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have `ban` permissions!")
        else:
            await ctx.send("You do not have `ban` permissions!")
    @commands.command(description="Remove Special Characters(Non Alphanumeric/Space) From Everyone's Diplay Name", help="decancer", aliases=["removecancerouscharacters"])
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def decancer(self, ctx):
      await ctx.send("Starting ETA: Now")
      start_time=time.time()
      changed=[]
      failed=[]
      for member in ctx.guild.members:
        name=member.nick or member.name
        original_name=name
        name=list(name)
        num=0
        for letter in name:
          if letter.lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7''8','9','0']:
            num=num+1
            continue
          else:
            name[num]=""
            num=num+1
        if name==[]:
          newname="Breh this guy though"
        else:
          newname="".join(name)
        if newname==original_name:
          continue
        else:
          try:
            await member.edit(nick=newname)
            changed.append(f"`{member}`")
          except:
            failed.append(f"`{member}`")
            continue
      timetaken=round(time.time()-start_time, 2)
      if changed==[]:
        await ctx.send("Decancered 0 members")
      else:
        texttosend="\n".join(changed)
        embed=discord.Embed(title=f"Decancered {len(changed)} Member(s)",description=texttosend,color=0x00FF00)
        await ctx.send(embed=embed)
      if failed==[]:
        await ctx.send("None failed to decancer")
      else:
        texttosend="\n".join(failed)
        embed=discord.Embed(title=f"Failed To Decancer {len(failed)} Member(s)",description=texttosend,color=0xFF0000)
        await ctx.send(embed=embed)
      await ctx.send(f"Time taken: `{timetaken}s`")
    @decancer.error
    async def decancer_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have `manage nickname` permissions!")
        else:
            await ctx.send("You do not have `manage nickname` permissions!")
    @commands.command(description="Change The Name Of Everyone Who's Display Name Begins Without An Alphanumeric Character To A Given Name/A Name Generated By The Bot", help="dehoist [new name]", aliases=["removehoist"])
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def dehoist(self, ctx, newname=None):
      await ctx.send("Starting ETA: Now")
      start_time=time.time()
      def string(length):
        chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        string=""
        length=int(length)
        for i in range(0,length):
          choice=random.choice(chars)
          string=string+random.choice(choice.lower()+choice.upper())
        return string
      changed=[]
      failed=[]
      shortened=False
      randomstring=False
      if newname is None:
        randomstring=True
      else:
        if len(newname)>=31:
          newname=newname[0:32]
          shortened=True
        else:
          newname=newname
      for member in ctx.guild.members:
        name=member.nick or member.name
        if list(name)[0].lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7''8','9','0']:
          continue
        else:
          if randomstring==True:
            newname="Hoisted User "+string(5)
          try:
            await member.edit(nick=newname)
            changed.append(f"`{member}`")
          except:
            failed.append(f"`{member}`")
      timetaken=round(time.time()-start_time, 2)
      if changed==[]:
        await ctx.send("Dehoisted 0 members")
      else:
        texttosend="\n".join(changed)
        embed=discord.Embed(title=f"Dehoisted {len(changed)} Member(s)",description=texttosend,color=0x00FF00)
        await ctx.send(embed=embed)
      if failed==[]:
        await ctx.send("None failed to dehoist")
      else:
        texttosend="\n".join(failed)
        embed=discord.Embed(title=f"Failed To Dehoist {len(failed)} Member(s)",description=texttosend,color=0xFF0000)
        await ctx.send(embed=embed)
      if shortened==True:
        await ctx.send("Note: I changed your given text to the first 32 characters, due to nickname length limitations.")
      await ctx.send(f"Time taken: `{timetaken}s`")
    @dehoist.error
    async def dehoist_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have `manage nickname` permissions!")
        else:
            await ctx.send("You do not have `manage nickname` permissions!")
    @commands.command(description="Remove All Nicknames In The Server", help="resetnick", aliases=["removenick"])
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def resetnick(self, ctx):
      for member in ctx.guild.members:
        if member.nick is None:
          continue
        else:
          await member.edit(nick=member.name)
      await ctx.send("Done")
    @resetnick.error
    async def resetnick_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have `manage nickname` permissions!")
        else:
            await ctx.send("You do not have `manage nickname` permissions!")
def setup(bot):
    bot.add_cog(Mod(bot))
