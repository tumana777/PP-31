# class Meta(type):
#     def __new__(mcls, name, bases, attrs):
#         for key, value in attrs.items():
#             if callable(value) and not key.startswith("_"):
#                 raise ValueError(f"Method must start with '_'!")
#
#         return super().__new__(mcls, name, bases, attrs)
#
#
# class MyClass(metaclass=Meta):
#
#     status = True
#
#     def _test(self):
#         return "Test"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# x = [str(elem) for elem in numbers]
#
# serialized_numbers = ', '.join(x)
#
# with open("numbers.txt", "w") as file:
#     file.write(serialized_numbers)

# with open("numbers.txt") as file:
#     data = file.read()
#
# deserialized_numbers = [int(elem) for elem in data.split(", ")]
#
# print(deserialized_numbers)



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student({self.name}, {self.age})"

st1 = Student("John", 20)

def student_serializer(obj):
    return {
        'Name': obj.name,
        'Age': obj.age
    }

serialized_student = student_serializer(st1)

def student_deserializer(data):
    return Student(data['Name'], data['Age'])

print(student_deserializer(serialized_student))













