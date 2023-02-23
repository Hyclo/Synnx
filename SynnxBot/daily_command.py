async def daily_run(ctx, discord, db, datetime, timeZone, random):
    bern_time = datetime.now(timeZone)
    bern_time = bern_time.strftime('%Y-%m-%d')
    embedVarDaily = discord.Embed(title=ctx.author.name + " used $daily",
                                  description="hopefully you get lucky",
                                  color=0xcc0066)
    user = db[ctx.author.name]
    if ctx.author.name in db.keys():
        if user["timeStampDaily"] != str(bern_time):
            randominteger = random.randint(1, 200)
            user.update({"coins": user["coins"] + randominteger})
            user.update({"timeStampDaily": bern_time})
            embedVarDaily.add_field(name=ctx.author.name + " got:",
                                    value=str(randominteger) + " new coins",
                                    inline=False)
            await ctx.respond(embed=embedVarDaily)
        else:
            await ctx.respond(
                ctx.author.name +
                " you have already claimed your coins for today")
