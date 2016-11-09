import csv
import module11

def read_file():
  with open('text.txt', 'r') as my_file:
    my_list = my_file.read()
    print(my_list)

def read_file_csv():
  with open('text.txt', 'r') as my_file:
    my_list = csv.reader(my_file)
    for i in my_list:
      print(','.join(i))

def main():
  read_file()
  print('=====================')
  read_file_csv()
  return

main()