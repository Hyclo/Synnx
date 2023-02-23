async def payrun_starter(db, channel):
    for key in db.keys():
        user = db[key]
        if "runningJob" in user.values():
            job = user["runningJob"]
            employee = job["employee"]
            pay = job["pay"]
            if user["coins"] > pay:
                if employee in db.keys():
                    DBofEmployee = db[employee]
                    DBofEmployee.update({"coins": pay + DBofEmployee["coins"]})
                    user.update({"coins": user["coins"] - pay})
                    await channel.send(
                        str(DBofEmployee) + "was paid by his employer")
            else:
                await channel.send(str(user) + " couldn't pay his employee")
