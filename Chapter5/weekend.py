import datetime
weekDays=("Monday","Tuesday","Wednesday", "Thursday", "Friday")
now=datetime.date.today()
dayOfWeek=now.weekday()
today=weekDays[dayOfWeek]
daysToWeekend=6-dayOfWeek
print(f"There are {daysToWeekend-1} days until the weekend.")
quotePrinted="false"
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today=="Sunday" and quotePrinted=="false":
        print(left, " Tomorrow starts the grind.")
        quotePrinted="true"
    elif (today=="Monday" or today=="Tuesday" or today=="Wednesday" or "Thursday") and quotePrinted=="false":
        print(left, " Class class class... you have class.")
        quotePrinted="true"
    elif today=="Friday" and quotePrinted=="false":
        print(left, " It's Friyay!")
        quotePrinted="true"
    elif quotePrinted=="false":
        print(left, "WEEKEND IS HERE!")
        quotePrinted="true"
    else:
        print(left)
