import datetime

current_time = datetime.date.today()
some_date = input('When your project is ower ? (dd/mm/yyyy) \n')
dead_line = datetime.datetime.strptime(some_date,'%d/%m/%Y').date()

difference = (dead_line - current_time).days

print(difference)

week_diff = difference/7
and_days = difference - int(week_diff)*7

print('We Have {0:.0f} weeks and {1:.0f} days when your project would over'.format(week_diff, and_days))
