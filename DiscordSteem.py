# Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from beem.exceptions import *
import asyncio
from beem.account import Account
import json
import requests
from beem.comment import Comment
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
from beem import Steem
from bson.errors import *


# Variables
bot = commands.Bot(command_prefix="!")
nodes = NodeList()
nodes.update_nodes()
stm = Steem(node=nodes.get_nodes())
set_shared_steem_instance(stm)
notes = {}

# Print When Ready
@bot.event
async def on_ready():
  print("Ready Sir!")

# Commands
@bot.command(pass_context=True)
async def blog(ctx, username, amount=3):
  try:
    acc = Account(username.lower())
    print(f"Someone asked for blog of {username}")
    embed = discord.Embed(title=("DiscordSteem"), description=(f"Last {amount} posts of {username}"), color=(0x00ff00))
    for post in acc.blog_history(limit=amount, reblogs=False):
      steem_link = f"https://steemit.com/@{post['author']}/{post['permlink']}"
      embed.add_field(name=(post["title"]), value=(f"[Check out this post by {post['author']}!]({steem_link})"))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
    print("Provided!")
  except AccountDoesNotExistsException:
    print("Someone wrote incorrect account name while using feed command")
    embed = discord.Embed(title=("DiscordSteem"), description=("The account doesn't exists!"), color=(0x00ff00))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def feed(ctx, username, amount=3):
  try:
    acc = Account(username.lower())
    print(f"Someone asked for feed of {username}")
    embed = discord.Embed(title=("DiscordSteem"), description=(f"This is the feed of {username}"), color=(0x00ff00))
    for post in acc.feed_history(limit=amount):
      steem_link = f"https://steemit.com/@{post['author']}/{post['permlink']}"
      embed.add_field(name=(post["title"]), value=(f"[Check out this post by {post['author']}!]({steem_link})"))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
    print("Provided!")
  except AccountDoesNotExistsException:
    print("Someone wrote incorrect account name while using feed command")
    embed = discord.Embed(title=("DiscordSteem"), description=("The account doesn't exists!"), color=(0x00ff00))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def comments(ctx, username, amount=3):
  try:
    acc = Account(username.lower())
    print(f"Someone asked for comments of {username}")
    embed = discord.Embed(title=("DiscordSteem"), description=(f"These are last {amount} comments of {username}"), color=(0x00ff00))
    for post in acc.comment_history(limit=amount):
      steem_link = f"https://steemit.com/@{post['author']}/{post['permlink']}"
      embed.add_field(name=(post["root_title"]), value=(f"[Check out this comment!]({steem_link})"))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
    print("Provided!")  
  except AccountDoesNotExistsException:
    print("Someone wrote incorrect account name while using comments command")
    embed = discord.Embed(title=("DiscordSteem"), description=("The account doesn't exists!"), color=(0x00ff00))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed) 

@bot.command(pass_context=True)
async def info(ctx, username):
  try:
    acc = Account(username.lower())
    print(f"Someone asked for info of {username}")
    embed = discord.Embed(title=(username), description=(acc.profile["about"]), color=(0x00ff00))
    profile = acc.json_metadata["profile"]
    embed.set_thumbnail(url=(profile["profile_image"]))
    embed.add_field(name=("Reputation"), value=(int(acc.rep)))
    embed.add_field(name=("Followers"), value=(len(acc.get_followers())))
    embed.add_field(name=("Accounts Following"), value=(len(acc.get_following())))
    embed.add_field(name=("Number Of Posts"), value=(acc["post_count"]))
    embed.add_field(name=("STEEM Balance"), value=(acc["balance"]))
    embed.add_field(name=("SBD Balance"), value=(acc["sbd_balance"]))
    embed.add_field(name=("Witnesses Voted"), value=(acc["witnesses_voted_for"]))
    embed.add_field(name=("Steem Power"), value=(f"{format(int(stm.vests_to_sp(acc['vesting_shares'])), ',d')} (+{format(int(stm.vests_to_sp(acc['received_vesting_shares'])), ',d')})"))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
    print("Provided!")
  except AccountDoesNotExistsException:
    print("Someone wrote incorrect account name while using info command")
    embed = discord.Embed(title=("DiscordSteem"), description=("The account doesn't exists!"), color=(0x00ff00))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)   

@bot.command(pass_context=True)
async def ticker(ctx, coin, currency="usd"):
  print(f"Someone asked for price of {coin} in {currency}")
  cur = currency.lower()
  r = requests.get(f"https://api.coinmarketcap.com/v1/ticker/{coin}/?convert={cur}")
  r_json = r.json()
  if type(r_json) is list:
    price = r_json[0].get(("price_" + cur), ("Invalid currency"))
    if price[0] == "I":
        print("Incorrect currency")
        embed = discord.Embed(title=("DiscordSteem"), description=("Invalid currency"), color=(0x00ff00))
        embed.set_footer(text="Developed By Rodux")
        await bot.say(embed=embed)
    else:
        print("Provided!")
        embed = discord.Embed(title=("Price Of " + coin.upper()), description=("%.3f %s" % (float(price), cur.upper())), color=(0x00ff00))
        embed.set_footer(text="Developed By Rodux")
        await bot.say(embed=embed)
  else:
    print("Incorrect coin")
    embed = discord.Embed(title=("DiscordSteem"), description=("Invalid coin"))
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def addnote(ctx, note):
  author = ctx.message.author
  if author in notes:
    notes[author] += [note]
    embed = discord.Embed(title="Note Added!", color=0x00ff00)
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)
  else:
    notes[author] = [note]
    embed = discord.Embed(title="Note Added!", color=0x00ff00)
    embed.set_footer(text="Developed By Rodux")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def note(ctx):
  author = ctx.message.author
  embed = discord.Embed(title=("DiscordSteem"), description=("Your Notes"), color=0x00ff00, inline=True)
  embed.set_footer(text="Developed By Rodux")
  for note in notes[author]:
    embed.add_field(name=note, value="Note")
  await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def delnote(ctx):
  author = ctx.message.author
  del notes[author]
  embed = discord.Embed(title="Notes Deleted!", color=0x00ff00)
  embed.set_footer(text="Developed By Rodux")
  await bot.say(embed=embed)

@bot.command(pass_context=True)
async def contributions(ctx, username, amount=3):
  try:
    i = 0
    acc = Account(username.lower())
    print(f"Someone asked for contributions of {username}")
    embed = discord.Embed(title="DiscordSteem", description=f"Utopian Contributions Of {username}", color=0x00ff00)
    embed.set_footer(text="Developed By Rodux")
    for post in acc.blog_history(limit=250, reblogs=False):
      steem_link = f"https://steemit.com/@{post['author']}/{post['permlink']}"
      if i != amount:
        if "utopian-io" in post["tags"]:
          if "tutorials" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Tutorials - [Check it out!]({steem_link})")
          elif "bug-hunting" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Bug-Hunting - [Check it out!]({steem_link})")
          elif "development" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Development - [Check it out!]({steem_link})")
          elif "graphics" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Graphics - [Check it out!]({steem_link})")
          elif "translations" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Translations - [Check it out!]({steem_link})")
          elif "video-tutorials" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Video-Tutorials - [Check it out!]({steem_link})")
          elif "ideas" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Ideas - [Check it out!]({steem_link})")
          elif "copywriting" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Copywriting - [Check it out!]({steem_link})")
          elif "documentation" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Documentation - [Check it out!]({steem_link})")
          elif "visibility" in post["tags"]:
            i += 1
            embed.add_field(name=post["title"], value=f"Visibility - [Check it out!]({steem_link})")
      else:
        await bot.say(embed=embed)
        print("Provided!")
        break
  except AccountDoesNotExistsException:
    embed = discord.Embed(title=("DiscordSteem"), description=("The account doesn't exists!"), color=(0x00ff00))
    embed.set_footer(text="Developed By Rodux")
    print("Someone wrote incorrect account name while using contributions command")
    await bot.say(embed=embed)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    print("Required Argument")
  elif isinstance(error, commands.MissingRequiredArgument):
    print("Missing Argument")

# Run The Bot
bot.run("TOKEN") # Replace Token
