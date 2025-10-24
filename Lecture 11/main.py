# def add(a:int, b:int):
#     return a + b
#
# print(add("a", "b"))
from string import punctuation

# from functools import reduce
#
# numbers = [2, 4, 7, 8, 9]
#
# print(reduce(lambda a, b: a + b, numbers, 5))

# def test(number=5):
#
#     total = 0
#
#     for i in range(number):
#         num = int(input(f"Please, input number {i + 1}: "))
#
#         total += num
#
#     return total
#
# print(test())

# import string
#
#
# def word_counter(text):
#     empty_dict = {}
#
#     lst = text.lower().split()
#
#     for word in lst:
#         if word not in empty_dict:
#             empty_dict[word.strip(string.punctuation)] = 1
#         else:
#             empty_dict[word.strip(string.punctuation)] += 1
#
#     return empty_dict
#
# print(word_counter("This is a test. This test is fun."))


# file = open('test.txt', 'r')
#
# print(file.read(35))
#
# # print(type(file.read()))
#
# # print(file.readable())
# # print(file.writable())
#
# print("second data")
#
# print(file.read())
#
# file.close()


# file = open('test.txt', 'r')
# print(file.read())
# file.seek(0)
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
#
# line1 = file.readline()
# line2 = file.readline()
#
# print(line2)
#
# file.close()

file = open('test.txt', 'r')

lines = file.readlines()

print(lines)

file.close()