async def sendMoney_run(ctx, discord, db, bern_time, random, target, amount):
    embedVarPay = discord.Embed(title="Payment has been sent ",description="",color=0x29a329)
    if amount <= 0:
        return
    if ctx.author.name in db.keys():
        user = db[ctx.author.name]
        if user["coins"] < int(amount):
            await ctx.respond(ctx.author.name + " you don't have enough coins, use $daily to get some")
        else:
            if target in db.keys():
                coins = amount
                user.update({"coins": user["coins"] - coins})
                targetUser = db[target]
                targetUser.update({"coins": targetUser["coins"] + coins})
                embedVarPay.add_field(
                    name="Infos: ",
                    value=target + " you have been paid: " +
                    str(amount) + " by " + ctx.author.name,
                    inline=False)
                await ctx.respond(embed=embedVarPay)
            else:
                await ctx.respond("your target doesn't exsist at the moment ask them to create a new account.")
