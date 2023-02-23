async def create_guild_event(message, client, bern_time, timedelta, datetime):
  if message.author.name == 'Lenillian':
    text_channel = client.get_channel(908337305759141956)
    
    announce_string = message.content.split('$announce ')[1]
    event_to_announce = announce_string.split('~')[0]
    n = announce_string.split('~')[1]
    time = announce_string.split('~')[2]

    startTime = datetime.strftime(bern_time + " " + n, "%m/%d/%Y, %H:%M:%S")
    endTime = time.strftime(bern_time + " " + time, "%m/%d/%Y, %H:%M:%S")
    
    starttime = startTime.isoformat()
    endtime =  endTime.isoformat()
    guild = client.GetGuild(908337305759141948)
    guildEvent = await guild.CreateEventAsync("Announcement: {0}".format(event_to_announce), starttime, 2, endtime, '<#908337305985638413>')   
    await text_channel.send(embed=guildEvent)