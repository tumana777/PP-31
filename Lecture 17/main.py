# grade = int(input("Enter your grade: "))
#
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")

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
#     @classmethod
#     def get_total_students(cls):
#         return cls.total_students
#
#     def get_email(self):
#         return f"{Student.status}.{self.last_name}@gmail.com"



# def change_value(func):
#     def wrapper(*args, **kwargs):
#         a = args[0] + 2
#         b = args[1] + 3
#         return func(a, b)
#     return wrapper
#
# @change_value
# def print_numbers(a, b):
#     print(f"a = {a}, b = {b}")
#
# print_numbers(1, 2)

# import time

# def test():
#     start = time.time()
#     print("Start")
#     time.sleep(2)
#     print("End")
#     end = time.time()
#     total = end - start
#     print(f"Total time: {total}")
#
# test()

# def time_counter(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Total time: {end - start}")
#         return result
#     return wrapper
#
# @time_counter
# def test(x, y):
#     print(x)
#     time.sleep(2)
#     print(y)
#
# test(5, 8)


# class Student:
#
#     def __new__(cls):
#         print("Called __new__ method")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("Called __init__ method")
#
#
#
# st1 = Student()


# class MyMeta(type):
#     def __new__(mcls, name, bases, attrs):
#         print(f"name: {name}")
#         print(f"bases: {bases}")
#         attrs['created_by'] = "Admin"
#         print(f"attrs: {attrs}")
#         return super().__new__(mcls, name, bases, attrs)
#
# class Parent:
#     pass
#
# class MyClass(Parent, metaclass=MyMeta):
#     status = True
#
# my_class = MyClass()
#
# print(my_class.created_by)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    # 12 -> 5 -> 10 -> 9 -> 8 -> 7

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# 12 -> 5 -> 10 -> 9 -> 8 -> 7

ll = LinkedList()

ll.append(5)
ll.append(10)
ll.append(9)
ll.append(8)
ll.append(7)
ll.append(6)
ll.prepend(12)

ll.print_list()
ll.delete(5)
ll.delete(5)
ll.delete(30)
#12 -> 5 -> 10 -> 8 -> 7
ll.print_list()































