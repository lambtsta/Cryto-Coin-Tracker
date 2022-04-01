import os
import discord
import requests
from replit import db
from webserver import keep_alive

client = discord.Client()

def getCryptoPrices(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['current_price'];
  return None;

def getCryptoName(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['name'];
  return None;

def getSlpValue(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=smooth-love-potion'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['current_price'];
  return None;

def getSlpName(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=smooth-love-potion'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['name'];
  return None;

def getBcoinValue(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=bomber-coin'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['current_price'];
  return None;

def getBcoinName(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=bomber-coin'
  r = requests.get(url=URL)
  data = r.json() 

  for i in range(len(data)):
    if data[i]['symbol'] == crypto:
      return data[i]['name'];
  return None;

@client.event 
async def on_ready():
    print('bot is online as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))
 
@client.event 
async def on_message(message):
    if message.author == client.user:
      return
      
    elif message.content in [coin for coin in db.keys()]: 
      embedVar = discord.Embed(title="Coin", description= getCryptoName(message.content.lower()), color=0x94C973)
      embedVar.add_field(name= "Current Value:", value= "₱ " + (str("{:,}".format(getCryptoPrices(message.content.lower())))), inline=True)
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/877724467177062454/949325724425261108/aaaa-removebg-preview.png")
      await message.channel.send( embed=embedVar)
  
    elif message.content.startswith('slp'):
      embedVar = discord.Embed(title="Coin", description= getSlpName(message.content.lower()), color=0x94C973)
      embedVar.add_field(name= "Current Value:", value= "₱ " + (str(getSlpValue(message.content.lower()))), inline=True)
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/877724467177062454/949325724425261108/aaaa-removebg-preview.png")
      await message.channel.send( embed=embedVar) 
      
    elif message.content.startswith('bcoin'):
      embedVar = discord.Embed(title="Coin", description= getBcoinName(message.content.lower()), color=0x94C973)
      embedVar.add_field(name= "Current Value:", value= "₱ " + (str(getBcoinValue(message.content.lower()))), inline=True)
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/877724467177062454/949325724425261108/aaaa-removebg-preview.png")
      await message.channel.send( embed=embedVar)

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)  