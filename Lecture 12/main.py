# file = open('test.txt', 'w')
#
# text = input("Enter your name: ")
#
# file.write(text)
#
# file.close()

# file = open('test.txt', 'a')
#
# text = input("Enter your name: ")
#
# file.write(f"{text}\n")
#
# file.close()

# file = open('names.txt', 'w')
#
# text = input("Enter your name: ")
#
# file.write(f"{text}\n")
#
# file.close()

# file = open('names.txt', 'x')
#
# text = input("Enter your name: ")
#
# file.write(f"{text}\n")
#
# file.close()

# file = open('names.txt', 'w+')
#
# print(file.writable())
# print(file.readable())
#
# file.close()

# file = open('names.txt', 'w+')
#
# names = ['otar', 'aleqs', 'giorgi', 'erekle', 'akaki', 'guliko', 'elisabed', 'nika', 'luka', 'ivane']
#
# new_names = [f"{elem}\n" for elem in names]
#
# file.writelines(new_names)
#
# file.close()

# with open('names.txt') as f:
#     data = f.readlines()
#
# print(f.read())

import os

# print(os.getcwd())

# print(os.listdir())

# if not os.path.exists('inner1'):
#     os.mkdir('inner1')
# else:
#     print('Folder already exists.')

# if os.path.exists('inner1'):
#     os.rmdir('inner1')
# else:
#     print('Folder does not exists.')

# os.remove('test.txt')


# if os.path.exists('inner'):
#     os.rmdir('inner')
#     print("Folder deleted successfully")
# else:
#     print('Folder does not exists.')

# import shutil
#
# shutil.rmtree('inner')

# name = "ოთარ"
#
# encoded_name = name.encode('utf-8')

# print(encoded_name)
# print(type(encoded_name))

# with open('name.bin', 'wb') as f:
#     f.write(encoded_name)

# with open('kw.jpeg', 'rb') as f:
#     data = f.read()
#
#     print(data)


# with open('../Lecture 11/main.py') as f:
#     print(f.read())

import csv

# with open('companies.csv') as csv_file:
#     reader = csv.reader(csv_file)
#
#     for row in reader:
#         print(row)

# first_row = ['name', 'age', 'city']
#
# names = [
#     ['otar', 34, 'Tbilisi', 58],
#     ['nino', 35, 'Zugdidi']
# ]
#
# with open('names.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#
#     writer.writerow(first_row)
#     writer.writerows(names)

# with open('names.csv') as csv_file:
#     reader = csv.DictReader(csv_file)
#
#     for row in reader:
#         print(row)


# names = [
#     {"name": "otar", 'age': 34, 'city': 'Tbilisi'},
#     {"name": "levan", 'age': 25, 'city': 'abasha'},
#     {"name": "nino", 'age': 34, 'city': 'Tbilisi'},
#     {"name": "ana", 'age': 34, 'city': 'Tbilisi'},
# ]

# headers = ['name', 'age', 'city']

# with open('names.csv', 'w') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=names[0].keys())
#
#     writer.writeheader()
#
#     writer.writerows(names)

# import faker
#
# fake = faker.Faker()
#
# for _ in range(10):
#     print(fake.email())