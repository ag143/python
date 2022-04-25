import datetime as dt
from datetime import datetime 

x = datetime.now()

print(x)
print("#####################")


x = datetime.now()

print(x.year)
print(x.strftime("%A"))
print("#####################")


x = datetime(2020, 5, 17)

print(x)

print("#####################")
from datetime import _datetime

x = datetime(2018, 6, 1)

print(x.strftime("%B"))
print("#####################")
