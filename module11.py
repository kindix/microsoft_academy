name_list = []
name = ''

while name != 'DONE':
  name = input('Write a few name (if you finish write DONE) \n')
  name_list.append(name)

name_list.remove('DONE')
name_list.sort()

counter = 1

f = open('text.txt', 'w')
for name in name_list:
  f.write('{0:d}, {1:s}\n'.format(counter,name))
  counter +=1
f.close()  

