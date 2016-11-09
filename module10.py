quests = ['Cris', 'Sus', 'Bill', 'Bill','3', '3', 'Cris']

#quests_clear = []
#for i in quests:
#  if i not in quests_clear:
#    quests_clear.append(i)
#print(quests_clear)

for i in range(4):
  if quests[i] == quests[i+1]:
    del quests[i]
print(quests)


#quests.append('Dick')

#del quests[-2]

#print(quests.index('Cris')) # = [0]


