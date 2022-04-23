from discord.ext import commands



bot = commands.Bot(command_prefix ='!')



@bot.command()

async def info(ctx):



  await ctx.send(ctx.guild)

  await ctx.send(ctx.author)

  await ctx.send(ctx.message.id)



bot.run('OTY0NDQ2MTc4MDE4MjA1NzA2.Ylkwfw.2vU0WFjVwhxRHJ0M0pvuujbXVoo')