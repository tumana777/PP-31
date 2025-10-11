# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]
#
# total = 0
#
# for product in products:
#     for key, value in product.items():
#         print(key)
#         total += value["price"] * value["quantity"]
#
#
# fruits = {}
#
# while True:
#     fruit = input('Enter a fruit name: ')
#
#     if fruit == 'stop':
#         break
#
#     if fruit in fruits:
#         fruits[fruit] += 1
#     else:
#         fruits[fruit] = 1
#
# print(fruits)

# num1 = int(input("Please enter number1: "))
# num2 = int(input("Please enter number2: "))
#
# print(num1 + num2)

# def sum_numbers():
#     num1 = int(input("Please enter number1: "))
#     num2 = int(input("Please enter number2: "))
#
#     print(num1 + num2)
#
# print("code executed")
# print("another code executed")
#
# sum_numbers()
#
#
# print("code 2 executed")
# print("another code executed also")
#
#
# sum_numbers()

# def sum_numbers(num1, num2):
#
#     result = num2 + num1
#
#     print(result)
#
# sum_numbers(8, 5)

# def substruct(num1, num2):
#     print(num2 - num1)
#
# substruct(8, 6)

# def sum_numbers(num1, num2):
#     print("function started")
#     return num2 + num1
#
# print("function ended")
#
#
# result1 = sum_numbers(2, 5)
# result2 = sum_numbers(8, 6)
#
# print(result1)
# print(result2)