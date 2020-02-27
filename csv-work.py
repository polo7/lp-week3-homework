import csv


user_list = [
	{'name': 'Masha', 'age': 25, 'job': 'Scientist'},
	{'name': 'Vasya', 'age': 8, 'job': 'Programmer'},
	{'name': 'Eduard', 'age': 48, 'job': 'Big boss'},
]

with open('export.csv', 'w', encoding='utf-8') as output_file:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(output_file, fields, delimiter=';')
	writer.writeheader()
	# for user in user_list:
	# 	writer.writerow(user)
	writer.writerows(user_list)
	print('Файл export.csv создан с указанными данными.')

