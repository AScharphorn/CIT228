import datetime
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Fridday", "Saturday", "Sunday")
now = datetime.date.today()
dayOfWeek = now.weekday()
today = weekdays[dayOfWeek]
daysToWeekend = 6-dayOfWeek

print("You have", daysToWeekend-1, "Days until you reach the weekend")
quotePrinted = "false"

if today == "Sunday" and quotePrinted == "false":
    print("Sunday is the best day!")
    quotePrinted = "true"
elif(today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
    print("The week just got started...")
    quotePrinted = "true"
elif(today == "Thursday" and quotePrinted == "false"):
    print("So close to the weekend...")
    quotePrinted = "true"
elif(quotePrinted == "false"):
    print("It is the weekend!")
    quotePrinted = "true"
else:
    print()