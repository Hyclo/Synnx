async def richest_run(ctx, discord, db, random, client):
    embedVar3 = discord.Embed(title="Richest Users on the server are: ", description="list of the richest five users", color=0xcc0066)
    all_users = {}
    list = {}
    counter = 0

    for key in db.keys():
        user = db[key]
        all_users[key] = user["coins"]
        
    sorted_list = sorted(all_users,key=all_users.get,  reverse=True)

    for key in sorted_list:
      if counter <= 4:
          counter = counter + 1
          userDB = db[key]
          list[key] = userDB["coins"]

    for key in list:
        embedVar3.add_field(name="{0} has:".format(key), value=str(db[key]["coins"]) + " coins", inline=False)
    await ctx.respond(embed=embedVar3)
