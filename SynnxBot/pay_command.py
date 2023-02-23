async def createJob_run(message, db):
    clearString = message.content.split("$createJob ", 1)[1]
    employee = clearString.split()[0]
    pay = clearString.split()[1]
    employer = db[message.author.name]
    if "runningJob" in employer.values():
        await message.channel.send(
            "you already have a running job, delete that first")

    if employee in db.keys():
        employer["runningJob"] = {"employee": employee, "pay": pay}
    else:
        message.channel.send(
            "your employee doesn't have an account ask them to create one")
        return
