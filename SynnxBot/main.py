import discord
from discord.ext import tasks, commands
from discord.commands.context import ApplicationContext
from discord.commands import Option
import os
from replit import db
from datetime import datetime, timedelta
import random
import pytz

#file imports starts here:
from daily_command import daily_run
from richest_command import richest_run
from dice_command import dice_run, allIn_run
from rob_command import rob_run
from sendMoney_command import sendMoney_run
from pay_command import createJob_run
from payrun_command import payrun_starter
from announcement_command import create_guild_event
from level_system import level_run, level
from stock_market import market_daily, market_run
from slot_machine import slot_machine_run
#file imports end here;
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

timeZone = pytz.timezone('Europe/Berlin')
bern_time = datetime.now(timeZone)
bern_time = bern_time.strftime('%Y-%m-%d')

bot = commands.Bot()

default_Db = {
    "coins": 0,
    "timeStampDaily": bern_time,
    "exp": 0,
    "level": 0,
    "stock_name": "none",
    "quantity": 0,
    "buy_price": 0
}

text_channel = bot.get_channel(978033714573488169)
payment_cannel = bot.get_channel(982341592654434334)
de_tisch_channel = bot.get_channel(908337305985638413)


def init_db(ctx):
    if ctx.author.name == 'MEE6':
        return
    if ctx.author.name == 'boti_the_bot':
        return

    if ctx.author.name in db.keys():
        ctx.respond("you already have an account")
    else:
        db[ctx.author.name] = default_Db
        ctx.respond("your account was succesfully created")


@tasks.loop(hours=24)
async def runningJobs():
    await payrun_starter(db, payment_cannel)


@bot.event
async def on_ready():
    print('We have logged in as {0.user} '.format(bot) +
          str(datetime.now(timeZone)))


#Level command


@bot.slash_command(name="level", description="show your level")
async def slash_level(ctx: discord.ApplicationContext):
    await level(db, discord, ctx)


#Daily cimmand


@bot.slash_command(name="daily")
async def slash_daily(ctx: discord.ApplicationContext):
    await daily_run(ctx, discord, db, datetime, timeZone, random)


#Richest command


@bot.slash_command(name="richest")
async def slash_richest(ctx: discord.ApplicationContext):
    await richest_run(ctx, discord, db, random, bot)


#Money command


@bot.slash_command(name="money")
async def slash_money(ctx: discord.ApplicationContext):
    embedVarAccount = discord.Embed(title=ctx.author.name + "s account",
                                    description="public account",
                                    color=0xcc0066)
    if ctx.author.name in db.keys():
        user = db[ctx.author.name]
        if ctx.author.name == "Lenillian":
            embedVarAccount.add_field(name="savingsaccount",
                                      value="Dad you have: {:d} coins".format(
                                          user["coins"]),
                                      inline=False)
            await ctx.respond(embed=embedVarAccount)
        else:
            embedVarAccount.add_field(
                name="savingsaccount",
                value=ctx.author.name +
                " you have: {:d} coins".format(user["coins"]),
                inline=False)
            await ctx.respond(embed=embedVarAccount)
    else:
        await ctx.respond(ctx.author.name +
                          " you don't have enough use $daily to get some")


#Dice command


@bot.slash_command(name="dice")
async def slash_dice(ctx: discord.ApplicationContext,
                     dice_amount: Option(int,
                                         "Give an amount to dice",
                                         required=True,
                                         default='')):
    await dice_run(ctx, discord, db, bern_time, random, dice_amount)


'''
@bot.slash_command(name="slotmachine")
async def slash_slot(ctx: discord.ApplicationContext, dice_amount: Option(
    int,
    "Give an amount to put in the slot machine",
    required=True,
    default='')):
    await slot_machine_run(ctx, discord, db, bern_time, random, bot)
'''

#All in command


@bot.slash_command(name="allin")
async def slash_all_in(ctx: discord.ApplicationContext):
    await allIn_run(ctx, discord, db, bern_time, random, bot)


#Send money command


@bot.slash_command(name="sendmoney")
async def slash_send_money(
    ctx: discord.ApplicationContext, amount: Option(int,
                                                    "amount you want to send",
                                                    required=True,
                                                    default=''),
    target: Option(str,
                   "target you want to send the money to",
                   required=True,
                   default='')):
    await sendMoney_run(ctx, discord, db, bern_time, random, target, amount)


#Login command (to int DB account)


@bot.slash_command(name="login",
                   description="create an account to stash your money")
async def slash_login(ctx: discord.ApplicationContext):
    await init_db(ctx)


##DEV OPERATIONS START##


@bot.slash_command(name="test")
async def slash_test(ctx: discord.ApplicationContext,
                     amount: Option(int,
                                    "Give an amount to test",
                                    required=True,
                                    default='')):
    user = db["Lenillian"]
    user.update({"coins": amount})
    await ctx.respond("brenn")


##DEV OPERATIONS END##


@bot.event
async def on_message(message):

    #if message.author.name == 'golfagent':
    # await message.delete()

    #blacklist(message)

    #init_db(message)

    #currentChannel = message.channel

    #-> level system

    await level_run(db, message, random, discord)

    #New method -> output the users money

    # if message.content == '$money':

    #await message.delete()

    #New method -> output all commands except dev commands

    #New method -> roll the dice against Synnx


"""
    if message.content.startswith('$dice'):
        return

    #New Method -> go all in just in one command

    if message.content.startswith('$all in'):
        return

    #New method -> send money to another user

    if message.content.startswith('$sendMoney'):
      return

    #New method -> shows the last timestamp that is saved to an account plus cuurent timestamp

    if message.content == '$showTimeStamp':
        user = db[message.author.name]
        await currentChannel.send(message.author.name +
                                  " your current time stamp is: " +
                                  str(user["timeStampDaily"]) + " today is: " +
                                  str(bern_time))
        await message.delete()

    #New method -> rob other player

    if message.content.startswith('$rob'):
        await rob_run(message, discord, db, bern_time, random, client,
                      username)
        await message.delete()

    #New method -> create jobs to pay other players on a daily basis

    if message.content.startswith("$createJob"):
        await createJob_run(message, db)
        await message.delete()

    #New Method -> announce something in chat

    if message.content.startswith('$announce'):
        await create_guild_event(message, client, bern_time, timedelta,
                                 datetime)
        await message.delete()

    #New Method -> buy stocks from market

    if message.content.startswith('$buy'):
        await market_run(message.channel, message, db)
        await message.delete()

    #New Method -> slot machine

    if message.content.startswith('$slot '):
        await slot_machine_run(message, discord, db, bern_time, random, client,
                               username)
        await message.delete()

    #New Method -> migrate user

    if message.content.startswith('$migrate'):
        if message.author.name == 'Lenillian':
            user = db[message.content.split('$migrate ')[1]]
            coins = user["coins"]
            timeStampDaily = user["timeStampDaily"]
            exp = user["exp"]
            clevel = user["level"]

            del db[message.content.split('$migrate ')[1]]

            db[message.content.split('$migrate ')[1]] = default_Db

            user = db[message.content.split('$migrate ')[1]]

            user.update({"coins": coins})
            user.update({"timeStampDaily": timeStampDaily})
            user.update({"exp": exp})
            user.update({"level": clevel})

    #DEV method

    if message.content.startswith('$setLevel'):
        if message.author.name == 'Lenillian':
            user = db["Lenillian"]
            user.update({"level": 23})

    if message.content.startswith('$sendAll'):
        if message.author.name == 'Lenillian':
            coins = int(message.content.split('$sendAll ')[1])
            for key in db.keys():
                user = db[key]
                user.update({"coins": user["coins"] + coins})

    if message.content == '$startJobs':
        if message.author.name == 'Lenillian':
            await runningJobs.start()

    if message.content == '$test2486':
        if message.author.name == 'Lenillian':
            user = db["Lenillian"]
            user.update({"coins": 0})

    if message.content == '$test6842':
        return

    if message.content == '$myCode?':
        if message.author.name == 'Lenillian':
            await currentChannel.send("du cracky mach din code besser")

    if message.content == '$printDB':
        if message.author.name == 'Lenillian':
            embedVarDevDB = discord.Embed(
                title="Dev Method",
                description="list of all the DB keys",
                color=0xcc0066)
            for i in db.keys():
                embedVarDevDB.add_field(name=i, value=db[i], inline=False)
            await currentChannel.send(embed=embedVarDevDB)

    if message.content == '$deleteDB':
        if message.author.name == 'Lenillian':
            for i in db.keys():
                del db[i]

    if message.content == '$deleteME':
        if message.author.name == 'Lenillian':
            del db['Lenillian']

    if message.content.startswith('$delete'):
        if message.author.name == 'Lenillian':
            del db[message.content.split('$delete ')[1]]

    if message.content == '$initMarket':
        if message.author.name == 'Lenillian':
            db["market"] = default_shop

"""

bot.run(os.environ['token'])
