import random

for steps in range(10):
  num1 = random.randrange(1,10)
  num2 = random.randrange(1,10)
  print('What rezult? {0:d} + {1:d}'.format(num1,num2))
  answer = int(input())    
  if answer != num1 + num2:
    break
