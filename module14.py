import sys

first_num = float(input())
second_num = float(input())

try:
	rezult = first_num / second_num
	print('{0:0.1f} / {1:0.1f} = {2:0.1f}'.format(first_num, second_num, rezult))

except:
	error = sys.exc_info()[0] #виводить помилку по назві класу
	print(error)

finally:
	print('finaly')