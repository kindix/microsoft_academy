import datetime

my_date = datetime.date.today()

print(my_date)

def format_date(date):
  cool_date = date.strftime('%d %b %Y')
  return cool_date
  
print(format_date(my_date))
