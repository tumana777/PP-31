import json
import pickle


# student = {
#     'name': 'John',
#     'age': 20,
#     'grades': [55, 65, 80, 75],
#     'status': True,
#     'pay': 1000.00,
#     'course': {
#         'name': 'Python',
#         'duration': 3
#     }
# }
#
# student1 = {
#     'name': 'Walter',
#     'age': 25,
#     'grades': [52, 48, 67, 73],
#     'status': False,
#     'pay': 1000.00,
#     'course': {
#         'name': 'Python',
#         'duration': 3
#     }
# }

# students = {
#     'students': [student, student1]
# }


# with open('students.json', 'w') as file:
#     json.dump(students, file, indent=4)

# student = {
#     'name': 'John',
#     'age': 20,
#     'grades': [55, 65, 80, 75],
#     'status': True,
#     'pay': 1000.00,
#     'course': {
#         'name': 'Python',
#         'duration': 3
#     },
#     1: 'test'
# }

# with open('student.json', 'w') as file:
#     json.dump(student, file, indent=4)

# with open('student.json', 'r') as file:
#     student = json.load(file)
#
# print(student)


# student = {
#     'name': 'John',
#     'age': 20,
#     'grades': [55, 65, 80, 75],
#     'status': True,
#     'pay': 1000.00,
#     'course': {
#         'name': 'Python',
#         'duration': 3
#     },
#     1: 'test'
# }
#
# student1 = {
#     'name': 'Walter',
#     'age': 25,
#     'grades': [52, 48, 67, 73],
#     'status': False,
#     'pay': 1000.00,
#     'course': {
#         'name': 'Python',
#         'duration': 3
#     }
# }
#
# students = [student, student1]
#
# serialized_students = json.dumps(students, indent=4)

# print(serialized_student)

# deserialized_students = json.loads(serialized_students)
#
# print(type(deserialized_students))



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# student2 = Student('John', 20)
#
# def student_serializer(obj):
#     return {
#         'student' : {'name': obj.name, 'age': obj.age}
#     }
#
# with open('student.json', 'w') as file:
#     json.dump(student2, file, indent=4, default=student_serializer)

# def student_deserializer(obj):
#     return Student(obj['name'], obj['age'])
#
# with open('student.json', 'r') as file:
#     student = json.load(file, object_hook=student_deserializer)
#
#
# print(student)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# student2 = Student('John', 20)


# serialized_student = pickle.dumps(student2)

# print(serialized_student)

# deserialized_student = pickle.loads(serialized_student)

# print(deserialized_student)

# with open('student.pkl', 'wb') as file:
#     pickle.dump(student2, file)
#
# with open('student.pkl', 'rb') as file:
#     student = pickle.load(file)
#
# print(student)

import requests

url = 'https://jsonplaceholder.typicode.com/todos'

# response = requests.get(url)
#
# if response.status_code == 200:
#     for todo in response.json():
#         print(todo)

test_data = {'title': 'Test task', 'completed': False}

serialized_data = json.dumps(test_data)

response = requests.post(url, json=test_data)

print(response.status_code)


































