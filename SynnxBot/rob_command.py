async def rob_run(message, discord, db, bern_time, random, client, username):

    embedVarSucceeded = discord.Embed(title="Robbing succeeded ",
                                      description="now run!",
                                      color=0x29a329)
    embedVarFailed = discord.Embed(title="Robbing failed ",
                                   description="damn what happened!",
                                   color=0xcc0000)
    embedVarNoUser = discord.Embed(title="No User to Rob",
                                   description="you can't rob a ghost!",
                                   color=0xcc0066)
    embedVarWrongChannel = discord.Embed(
        title="wrong channel ",
        description="this command is only awailable in a specific channel",
        color=0xcc0066)

    newString = message.content.split('$rob ')[1]
    userToRob = newString.split('try ')[1]

    text_channel = client.get_channel(978033714573488169)
    if message.channel.name == "bot-commands":
        if message.author.name in db.keys():
            if db[message.author.name]["coins"] >= 100:
                if userToRob in db.keys():
                    randomInteger = random.randint(0, 100)
                    if randomInteger < 30:
                        valueOfUserToRob = db[userToRob]["coins"]
                        if (valueOfUserToRob / 100) > 1:
                            db[userToRob].update({
                                "coins":
                                valueOfUserToRob - int(valueOfUserToRob / 100)
                            })
                            valueOfRobber = db[message.author.name]["coins"]
                            db[message.author.name].update({
                                "coins":
                                valueOfRobber + int(valueOfUserToRob / 100)
                            })
                            embedVarSucceeded.add_field(
                                name="Info: ",
                                value="target: " + userToRob + " payout: " +
                                str(int(valueOfUserToRob / 100)) + " coins",
                                inline=False)
                            await message.channel.send(embed=embedVarSucceeded)
                        else:
                            embedVarFailed.add_field(
                                name="Info: ",
                                value="your target: " + userToRob +
                                " has no money you can steal",
                                inline=False)
                            await message.channel.send(embed=embedVarFailed)
                    else:
                        valueOfRobber = db[message.author.name]["coins"]
                        db[message.author.name].update(
                            {"coins": valueOfRobber - int(valueOfRobber / 80)})
                        valueOfUserToRob = db[userToRob]["coins"]
                        db[userToRob].update({
                            "coins":
                            valueOfUserToRob + int(valueOfRobber / 80)
                        })
                        embedVarFailed.add_field(
                            name="Info: ",
                            value="your target: " + userToRob +
                            " saw you and charged you: " +
                            str(int(valueOfRobber / 80)) + " coins",
                            inline=False)
                        await message.channel.send(embed=embedVarFailed)
                else:
                    embedVarNoUser.add_field(name="Info: ",
                                             value="your target: " +
                                             userToRob +
                                             "does't exsist or has no money",
                                             inline=False)
                    await message.channel.send(embed=embedVarNoUser)
            else:
                embedVarFailed.add_field(
                    name="Info: ",
                    value=
                    "you don't have enough money to buy some weapons, and you can't rob your target with bare hands",
                    inline=False)
                await message.channel.send(embed=embedVarFailed)
        else:
            await message.channel.send(
                username + " you don't have a account yet, use $daily")
    else:
        embedVarWrongChannel.add_field(
            name="I'm sorry for the inconvenience".format(text_channel),
            value='use {0.mention}'.format(text_channel),
            inline=False)
        await message.channel.send(embed=embedVarWrongChannel)
