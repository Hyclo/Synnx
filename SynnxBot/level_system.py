async def level_run(db, message, random, discord):
  author = message.author
  if author.name == "Synnx":
    return
  if author.name in db.keys():
    user = db[author.name]
    currentLevel = user["level"]
    user.update({"exp": user["exp"] + random.randint(10,25)})
    if user["exp"] > (1000 * (currentLevel + 1)):
      embedLevel = discord.Embed(title="Congratulations you reached the next lvl: " + str(user["level"]+1) ,description="<@{0}> take some coins as a present".format(author.id), color=0xcc0066)
      user.update({"level": user["level"] + 1})
      user.update({"coins": user["coins"] + 10 * currentLevel})
      user.update({"exp": 0})
      await message.channel.send(embed=embedLevel)
      
      
async def level(db, discord, ctx):
  author = ctx.author
  if author.name in db.keys():
    user = db[author.name]
    embedCurrentLevel = discord.Embed(title="Level information:",description="you are level: " + str(user["level"]), color=0xcc0066)
    embedCurrentLevel.add_field(name="Experience Information:",value="you have " + str(user["exp"]) + "exp, you need " + str((1000 * (user["level"] + 1)) - user["exp"]) + "exp more for the next level", inline=False)
    embedCurrentLevel.add_field(name="User information:",value="your name is: <@{0}>".format(ctx.author.id), inline=False)
    await ctx.respond(embed=embedCurrentLevel)
  