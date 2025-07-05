import datetime
# from datetime import  datetime
print((len(dir(datetime))))
print(dir(datetime))
print(datetime.date.today())
print(datetime.date(2025,1,1))
print(datetime.date.max)
print(datetime.date.min)
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())
# print(datetime.datetime.)
print(datetime.datetime.now().strftime("%d-%b-%y"))

# Parsing Strings to Dates (strptime)
nowDate = "28-06-2025"
datetime.datetime.strptime (nowDate, "%d-%m-%Y")


