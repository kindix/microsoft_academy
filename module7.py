name = input('Enter your name \n').capitalize()
nick_name = input('Enter your nick name \n')

good_name = False
good_nick = False

if name == 'Andrey':
  good_name = True
  
if nick_name == 'kind':
  good_nick = True
  
if good_name and good_nick:
  print('Hello %s' %name)
else:
  print('I don\'t now who are you?')
