# class Student:
#     status = True
#     pay = 1000
#     total_students = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Student.total_students += 1
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def get_email(self, domain):
#         return f"{self.first_name}.{self.last_name}@{domain}"
#
#     def __repr__(self):
#         return f"Student({self.first_name}, {self.last_name}, {self.age})"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age} years old"
#
# student1 = Student('walter', 'white', 55)
# student2 = Student('jessie', 'pinkman', 30)

# print(student1)
# print(student2)
# print(student1.__repr__())
# print(student2.__repr__())

# print(student1 + student2)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return f"{other} is not a vector object"
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return f"{other} is not a vector object"
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# vect1 = Vector(1, 2)
# vect2 = Vector(3, 4)
#
# print(vect1 + vect2)
# print(vect1 - vect2)


# class Student:
#     pay = 1000
#     discount = 0.8
#
#     def __init__(self, first_name, last_name, pay, discount):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.discount = discount
#
#     def get_pay(self):
#         return self.pay * self.discount
#
#     @classmethod
#     def get_base_pay(cls):
#         return cls.pay * cls.discount
#
#     @staticmethod
#     def get_resting():
#         day = input("Enter day of the week: ").lower()
#
#         if day == "sunday":
#             return "You can rest today"
#         return "You can't rest today"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# student1 = Student('Walter', 'white', 700, 0.9)

# print(student1.get_pay())
# print(student1.get_base_pay())

# print(student1.get_resting())

# class Student:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self._last_name = last_name
#         self.__age = age
#
#     def __call__(self):
#         return "I am callable"
#
#     def get_last_name(self):
#         return self._last_name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age cannot be negative")
#         self.__age = value
#
# student1 = Student('walter', 'white', 55)

# print(student1.get_last_name())
# print(student1._Student__age)
# print(student1.age)
# student1.age = 20
# print(student1.age)

# print(student1())

#
# class Multiplier:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, other):
#         return self.value * other
#
#
# double = Multiplier(2)
# triple = Multiplier(3)
#
# print(double(8))
# print(double(7))
#
# print(triple(8))
# print(triple(7))











