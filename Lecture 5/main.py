# lst1 = []
# lst2 = list()

# print(len(lst1))
# print(len(lst2))

# int_list = [1, 2, 3, 4, 5]

# mixed_list = [1, "Hello", 3.14, 1, True, [2, 3, 4, 5]]
#
# mixed_list.append(100)
# mixed_list.append('Test')

# mixed_list.clear()

# copied = mixed_list.copy()
# lst2 = mixed_list

# print(id(mixed_list))
# print(id(copied))
# print(id(lst2))

# print(copied == mixed_list)
# print(copied is mixed_list)

# mixed_list.append("hello")
#
# print(mixed_list)
# print(copied)
# print(lst2)

# mixed_list = [5, "Otar", 36, 1]
#
# mixed_list1 = [1, "Hello", 3.14, 1, True, [2, 3, 4, 5], True, 3.14]

# print(len(mixed_list))

# print(mixed_list.count(True))

# print(mixed_list.count(3.14))

# mixed_list1.extend(mixed_list)
#
# print(mixed_list1)


# print(mixed_list1.index(3.14))


# mixed_list = [5, "Otar", 36, 1]

# mixed_list1 = [1, "Hello", 3.14, 1, True, [2, 3, 4, 5], True, 3.14]

# mixed_list1.insert(0, False)
# mixed_list1.insert(7, False)

# popped_item = mixed_list1.pop()
# mixed_list1.pop(3)

# print(popped_item)

# mixed_list1.remove(True)

# mixed_list1.reverse()

# for elem in mixed_list1:
#     if type(elem) == int and elem == 1:
#         mixed_list1.remove(elem)

# num_list = [2, 1, 4, 3, 5]

# names = ["Otar", "Aleks", "Aleksandar"]
#
# names.sort()

# num_list.sort(reverse=True)
#
# print(num_list)


mixed_list = [1, "Hello", 3.14, 1, True, [2, 3, 4, 5], True, 3.14]

# for i in range(len(mixed_list)):
#     print(f"{i}: {mixed_list[i]}")

# for elem in enumerate(mixed_list):
#     print(elem)

# for i, item in enumerate(mixed_list):
#     print(f"{i}: {item}")

# for item in mixed_list:
#     print(item)

# print(mixed_list[2:7:2])

# num1, num2 = 1, 2
#
# print(num1)


# num1, num2 = (1, 2)
#
#
# print(num1, num2)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(matrix[1][1])


# num_list = []
#
# for i in range(1, 11):
#     num_list.append(i)
#
# print(num_list)

# nums = [i for i in range(1, 11)]
#
# print(nums)

# words = ["Hello" for _ in range(1, 11)]
#
# print(words)

nums = [i ** 2 for i in range(1, 21) if i % 2 == 0]

print(nums)

# num_list = []
#
# for i in range(1, 21):
#     if i % 2 == 0:
#         num_list.append(i)
#
# print(num_list)


