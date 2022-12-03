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
        
