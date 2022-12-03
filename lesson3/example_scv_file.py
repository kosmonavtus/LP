import csv

user_list = []
with open('lesson3/example.csv','r') as file:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(file, fields, delimiter=';')
    for row in reader:
        user_list.append(row)

with open('lesson3/export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    for user in user_list:
        writer.writerow(user)
        
lit_of_dict =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
with open('lesson3/lit_of_dict.csv', 'w') as lit_of_dict_file:
    fields2 = ['name', 'age', 'job']
    csvwriter = csv.DictWriter(lit_of_dict_file, fields2, delimiter=';')
    for object in lit_of_dict:
        csvwriter.writerow(object)