import csv

with open('text.txt', 'r') as my_file:
  all_names = csv.reader(my_file)
 
  for one_by_one_item in all_names:
    print(','.join(one_by_one_item))
    for item in one_by_one_item:
      print(item)
  

