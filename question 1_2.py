
import discord

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)




@client.event
async def on_member_join(member):
  general_channel: discord.TextChannel = client.get_channel(964448340362297357)
  await general_channel.send(content="Bienvenue sur le serveur {member.display_name} !")

client = discord.Client()

@client.event
async def on_ready():
  print("le bot est pret")

@client.event
async def on_message(message):
  if message.content.lower() == "ping":
    await message.channel.send("pong", delete_after=5)

  if message.content.startswith("!del"):
    number = int(message.content.split()[1])
    messages = await message.channel.history(limit=number +1).flatten()
  for each_message in messages: await each_message.delete()
 

   
   

client.run("OTY0NDQ2MTc4MDE4MjA1NzA2.Ylkwfw.2vU0WFjVwhxRHJ0M0pvuujbXVoo")        