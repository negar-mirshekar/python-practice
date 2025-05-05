from datetime import date
from datetime import datetime
from datetime import timedelta


today = date.today()

print("today's date : {}".format(today))

print("Date : " , today.day , today.month , today.year )

print("Today's weekday: ", today.weekday())



now = datetime.now()

print("the current date and time is : ", now)

print(now.strftime(" %A, %d, %b, %Y - %I:%M:%S %p"))

print(timedelta(days=365 , hours= 8))


time = datetime.now() + timedelta(days=365, weeks=8, hours=12)
print("one year from now : " , time)