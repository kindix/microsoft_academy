import datetime

current_time = datetime.date.today()

print(current_time)
print(current_time.month)
print(current_time.day)
print(current_time.strftime('%d %b %y'))




birthday = input('When your project is ower ? (dd/mm/yyyy) \n')
birthdate = datetime.datetime.strptime(birthday,'%d/%m/%Y').date()

difference = birthdate - current_time

print(difference.days)

time_now = datetime.datetime.now()

print(time_now.strftime('%H:%M:%S'))
