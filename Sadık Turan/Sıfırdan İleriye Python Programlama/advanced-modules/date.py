from datetime import datetime
from datetime import timedelta
# from datetime import time
# from datetime import date
# import datetime

# result = dir(datetime.datetime)
# result = dir(datetime.date)
# result = dir(datetime.time)
simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = datetime.now().year
result = datetime.now().month
result = datetime.now().day
result = datetime.now().hour
result = datetime.now().minute
result = datetime.now().second
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")
result = datetime.strftime(simdi,"%X")
result = datetime.strftime(simdi,"%d")
result = datetime.strftime(simdi,"%A")
result = datetime.strftime(simdi,"%B")
result = datetime.strftime(simdi,"%Y %B %A")

# t = '21 Nisan 2019'

# gun , ay , yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
# print(dt)

birthday = datetime(1999,2,14,10,30,00)
result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)
result = datetime.fromtimestamp(0)

result = simdi - birthday #time delta
# result = result.days
result = result.seconds


result = simdi + timedelta(days=10)
result = simdi + timedelta(days=730)
print(result)