name_list = []
name = ''

while name != 'DONE':
  name = input('Write a few name (if you finish write DONE) \n')
  name_list.append(name)

name_list.remove('DONE')
name_list.sort()

counter = 1

for name in name_list:
  print('{0:d}: {1:s}'.format(counter,name))
  counter +=1


