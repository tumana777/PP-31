# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Alex', 'Lewis', 45),
#     ('Alex', 'Rush', 65),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# while True:
#     name = input("Enter a name: ").lower()
#
#     if name == "stop":
#         break
#
#     found_persons = [person for person in persons if name == person[0].lower()]
#
#     # for person in persons:
#     #     if name == person[0].lower():
#     #         found_persons.append(person)
#
#     if found_persons:
#         last_name = input("Enter a last name: ").lower()
#
#         for person in found_persons:
#             if last_name == person[1].lower():
#                 print(f"{person[0]} {person[1]} is {person[2]} years old.")
#                 break
#         else:
#             print("no last name found")
#     else:
#         print("no name found")

# def add(*args):
#
#     total = 0
#
#     for num in args:
#         total += num
#
#     return total
#
# print(add(1, 9, 7))

# def add(num1, num2, *args):
#     return f"num1 = {num1}, num2 = {num2}, args = {args}"
#
# print(add(4, 8, 7, 9))


# *a, b, c = 1, 5, 7, 9
#
# print(a, b, c)

# def add(a, b):
#     return a + b
#
# lst = [5, 7]

# a, b = lst

# print(a, b)

# print(add(*lst))


# def add(a, b):
#     return a + b
#
# tuple1 = (1, 2)
#
# print(add(*tuple1))

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# print(greet("Otar", "Hi"))

# def greet(name, greeting, age):
#     return f"name = {name}, greeting = {greeting}, age = {age}"
#
# print(greet("Otar", greeting="Hi", age=34))

# def greet(*args, **kwargs):
#     return f"args = {args}, kwargs = {kwargs}"
#
# print(greet("Test", "test2", name="Otar", greeting="Hi", age=34))

x = 10 #Global

__name__ = "global name"

def outer():
    # x = 8 #Enclosing
    __name__ = "enclosing name"

    def inner():
        # x = 5 #Local
        __name__ = "local name"
        print(__name__)

    inner()

outer()








