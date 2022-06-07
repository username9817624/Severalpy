import datetime

date_var = datetime.datetime.now()
print(date_var.strftime("Time: %X\nDate: %d/%m/%y\nDate: %d %A/%m %B/%Y\nWeek: %W"))
input('')
