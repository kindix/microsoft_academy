man_live = input('Where do you live? \n').capitalize()
man_price = int(input('Put your price : '))

if man_live == 'Country':
  tax = 0.07
elif man_live == 'Vilage':
  tax = 0.05

all_price = man_price*(1+tax)
print('You must to pay {0:0.2f} $'.format(all_price)) 
