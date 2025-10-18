# def add(a, b):
#     return a + b
#
# def substruct(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# def test(func, a, b):
#     if callable(func):
#         return func(a, b)
#     return "Not a function"
#
# print(test(9, 5, 3))
# print(test(substruct, 5, 3))
# print(test(multiply, 5, 3))
# print(test(divide, 5, 3))

# func_list = [add, substruct, multiply, divide]
#
# for func in func_list:
#     print(test(func, 5, 3))

# def get_multiplier(a):
#     def multiplier(b):
#         return a * b
#     return multiplier

# print(get_multiplier(6)(9))

# multiply_by_5 = get_multiplier(5)

# print(multiply_by_5(8))
# print(multiply_by_5(74))
# print(multiply_by_5(4))
# print(multiply_by_5(13))

# multiply_by_8 = get_multiplier(8)
#
# print(multiply_by_8(8))
# print(multiply_by_8(12))
# print(multiply_by_8(20))
# print(multiply_by_8(10))

# print(callable(multiply_by_5))


# print(callable(print))

# def find_factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * find_factorial(n - 1) # 5 * 4 * 3 * 2 * 1
#
# print(find_factorial(0))

# test = lambda a: a * 2
#
# print(test(5))

# test = lambda a, b: a + b
#
# print(test(5, 3))

# def check_len(x):
#     return len(x)

# names = ["john", "jane", "jeremy", "walter", "jessy", "soul"]

# new_names = map(lambda x: x.capitalize(), names)
#
# print(list(new_names))

# names_length = map(lambda x: len(x), names)
#
# print(list(names_length))


# names = ["john", "jane", "jeremy", "walter", "jessy", "soul"]
#
# long_names = filter(lambda x: len(x) > 4, names)
#
# print(list(long_names))

# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
#
# print(reduce(lambda a, b: a + b, numbers))

# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a, reverse=True)
# print(x)

# names = ["john", "jan", "jeremy", "walter", "jessy", "soul"]
#
# print(sorted(names, key=lambda x: len(x)))


# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
# except ValueError:
#     print("Invalid integer")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print(result)
# finally:
#     print("This code will execute no matter what")