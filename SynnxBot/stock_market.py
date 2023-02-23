async def market_run(channel, message, db):
  new_string = message.content.split('$buy ')[1]
  quantity = new_string.split(' ')
  stock_name = new_string.split(' ')[1]
  author = message.author
  author_db = db[author.name]
  market = db['market']

  if author_db["stock_name"] != 'none':
    await channel.send("you already bought some stocks, sell them first")
  else:
    for index in market:
      if stock_name == author_db['stock_name']:
        author_db.update({"quantity": int(quantity)})
        author_db.update({"stock_name": stock_name})
        index.update({"quantity" - int(quantity)})
        price = int(quantity) * index["value"]
        author_db.update({"coins": author_db["coins"] - price})
        await channel.send("you bought {0} of {1}".format(quantity, stock_name))
      else: 
        await channel.send("this stock doesn't exsist!")
      

async def market_daily(db, random):
  market = db["market"]
  hard_market_change = 0
  change_value = 0
  
  for index in market:
    extreme = random.randint(0,1)
    if extreme == hard_market_change:
      change_value = random.randint(25,50)
    else:
      change_value = random.randint(0,24)

    plus_or_minus = random.randint(0,1)
  
    if plus_or_minus == 0:
      index.update({"value": index["value"] + change_value})
    else:
      if index["value"] - change_value <= 10:
        index.update({"value": 10})
      else:
        index.update({"value": index["value"] - change_value})


async def show_market(db, channel):
  return