async def slot_machine_run(ctx, discord, db, bern_time, random, client,
                           username):
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
    gamblingCoins = message.content.split("$slot ", 1)[1]
    channel = message.channel
    channel_name = channel.name
    author_name = message.author.name

    if channel_name == "bot-commands":
        await slot_run(author_name, db, gamblingCoins, ctx, random,
                       message, embedVarWon, embedVarLose)
    else:
        embedVarWrongChannel.add_field(name="I'm sorry for the inconvenience",
                                       value='use <#978033714573488169>',
                                       inline=False)
        await channel.send(embed=embedVarWrongChannel)


from collections import Counter

win_multipliers = {3: 4, 4: 50, 5: 1100, 6: 100000}


async def slot_run(author_name, db, gamblingCoins, ctx, random, message,
                   embedVarWon, embedVarLose):
    if author_name in db.keys():
        user = db[author_name]
        if int(gamblingCoins) <= 0:
            await channel.send(author_name +
                               " you silly we won't play for nothing")
        else:
            if user["coins"] < int(gamblingCoins):
                await channel.send(
                    author_name +
                    " you don't have enough coins use $daily to get some")
            else:
                await randomSeed(random)
                firstRoll = random.randint(1, 9)
                await randomSeed(random)
                secondRoll = random.randint(1, 9)
                await randomSeed(random)
                thirdRoll = random.randint(1, 9)
                await randomSeed(random)
                fourthRoll = random.randint(1, 9)
                await randomSeed(random)
                fifthRoll = random.randint(1, 9)
                await randomSeed(random)
                sixthRoll = random.randint(1, 9)

                rolls = [
                    firstRoll, secondRoll, thirdRoll, fourthRoll, fifthRoll,
                    sixthRoll
                ]
                counter = Counter(rolls)
                win = 0

                for i in counter.values():
                    if i > 2:
                        if i > win:
                            win = i

                if win <= 2:
                    embedVarLose.add_field(
                        name="You lose!",
                        value="<@{0}> you have [{1}|{2}|{3}|{4}|{5}|{6}]".
                        format(message.author.id, firstRoll, secondRoll,
                               thirdRoll, fourthRoll, fifthRoll, sixthRoll) +
                        " you lost " + str(gamblingCoins) + " coins!",
                        inline=False)
                    await ctx.respond(embed=embedVarWrongChannel)
                    user.update({"coins": user["coins"] - int(gamblingCoins)})
                else:
                    embedVarWon.add_field(
                        name="You won!",
                        value="<@{0}> you have [{1}|{2}|{3}|{4}|{5}|{6}]".
                        format(message.author.id, firstRoll, secondRoll,
                               thirdRoll, fourthRoll, fifthRoll, sixthRoll) +
                        " you won " +
                        str(int(gamblingCoins) * win_multipliers.get(win)) +
                        " coins!",
                        inline=False)
                    await channel.send(embed=embedVarWon)
                    user.update(
                        {"coins": user["coins"] + (int(gamblingCoins) * win)})


async def randomSeed(random):
    random.seed(random.randint(100, 100000000))
