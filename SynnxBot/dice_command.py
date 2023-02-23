async def dice_run(ctx, discord, db, bern_time, random, dice_amount):
    embedVarWon = discord.Embed(title="Game Result ",
                                description="damn go for it!",
                                color=0x29a329)
    embedVarLose = discord.Embed(title="Game Result ",
                                 description="yes give me all your money!",
                                 color=0xcc0000)
    embedVarWrongChannel = discord.Embed(
        title="wrong channel ",
        description="this command is only awailable in a specific channel",
        color=0xcc0066)

    channel = ctx.channel
    channel_name = channel.name
    author_name = ctx.author.name

    if channel_name == "bot-commands":
        await dice_heart(author_name, db, dice_amount, channel, random, ctx,
                         embedVarWon, embedVarLose)
    else:
        embedVarWrongChannel.add_field(name="I'm sorry for the inconvenience",
                                       value='use <#978033714573488169>',
                                       inline=False)
        await ctx.respond(embed=embedVarWrongChannel)


async def allIn_run(ctx, discord, db, bern_time, random, bot):
    embedVarWon = discord.Embed(title="Game Result ",
                                description="damn go for it!",
                                color=0x29a329)
    embedVarLose = discord.Embed(title="Game Result ",
                                 description="yes give me all your money!",
                                 color=0xcc0000)
    embedVarWrongChannel = discord.Embed(
        title="wrong channel ",
        description="this command is only awailable in a specific channel",
        color=0xcc0066)

    channel = ctx.channel
    channel_name = channel.name
    author_name = ctx.author.name

    dice_amount = db[author_name]["coins"]

    if channel_name == "bot-commands":
        await dice_heart(author_name, db, dice_amount, channel, random, ctx,
                         embedVarWon, embedVarLose)
    else:
        embedVarWrongChannel.add_field(name="I'm sorry for the inconvenience",
                                       value='use <#978033714573488169>',
                                       inline=False)
        await ctx.respond(embed=embedVarWrongChannel)


async def dice_heart(author_name, db, dice_amount, channel, random, ctx,
                     embedVarWon, embedVarLose):
    if author_name in db.keys():
        user = db[author_name]
        if dice_amount <= 0:
            await ctx.respond(author_name +
                              " you silly we won't play for nothing")
        else:
            if user["coins"] < int(dice_amount):
                await ctx.respond(
                    author_name +
                    " you don't have enough coins use $daily to get some")
            else:
                await randomSeed(random)
                userRoll = random.randint(1, 6)
                await randomSeed(random)
                botRoll = random.randint(1, 6)
                if userRoll > botRoll:
                    embedVarWon.add_field(
                        name="You won!",
                        value="<@{0}> you rolled a ".format(ctx.author.id) +
                        str(userRoll) + " I only " + str(botRoll) +
                        " you won " + str(dice_amount) + " coins!",
                        inline=False)
                    await ctx.respond(embed=embedVarWon)
                    user.update({"coins": user["coins"] + int(dice_amount)})
                elif userRoll == botRoll:
                    await ctx.respond(
                        ctx.author.mention +
                        " we rolled the same amount keep your coins")
                else:
                    embedVarLose.add_field(
                        name="You lose!",
                        value=ctx.author.mention + " you have rolled a " +
                        str(userRoll) + " I got a " + str(botRoll) +
                        " you lost " + str(dice_amount) + " coins!",
                        inline=False)
                    await ctx.respond(embed=embedVarLose)
                    user.update({"coins": user["coins"] - int(dice_amount)})


async def randomSeed(random):
    random.seed(random.randint(100, 100000000))
