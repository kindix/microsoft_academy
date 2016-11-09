user_pay = float(input('Put your amount \n'))

if user_pay < 50:
  user_pay = user_pay + 10
  print('You must to pay {0:0.2f} $'.format(user_pay ))
else:
  print('You must to pay %d $' %user_pay)
  
