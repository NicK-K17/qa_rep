import datetime

now = datetime.datetime.now()
print(now)

today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) # заменило на введенное значение
print(today_midnight)

print(now + datetime.timedelta(hours=10)) # Прибавило 10 часов



