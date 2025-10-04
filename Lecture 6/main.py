# text = input("Please, input sentence: ")
# word1 = input("Please, input word1: ")
# word2 = input("Please, input word2: ")
#
# text = text.replace(word1, word2)
#
# print(text)

# word1 = input("Enter a word1: ").lower()
# word2 = input("Enter a word2: ").lower()

# listen
# silent

# word3 = ''

# if len(word1) != len(word2):
#     print("The words are not anagrams")
# else:
#     for letter in word1:
#         if word1.count(letter) != word2.count(letter):
#             print("The words are not anagrams")
#             break
#     else:
#         print("The words are anagrams")

# if len(word1) != len(word2):
#     print("The words are not anagrams")
# else:
#     for letter in word1:
#         if word1.count(letter) == word2.count(letter):
#             word3 += letter
#
# if word3 == word1:
#     print("The words are anagrams")
# else:
#     print("The words are not anagrams")


# for letter in word1:
#     if letter in word2:
#         word2 = word2.replace(letter, "", 1)
#
# if word2 == '':
#     print("anagrams")
# else:
#     print("not anagrams")


# names = ['akaki', 'nika', 'elisabed', 'guliko', 'aleqsi', 'erekle', 'ivane']
#
# ages = [20, 25, 23, 18, 28, 19, 25]
#
# for i in range(len(names)):
#     print(names[i], ages[i])

# empty_dict = {}
#
# print(type(empty_dict))

# names = {
#     'akaki': 20,
#     'nika': 25,
#     'elisabed': 23,
#     'guliko': 20,
#     'aleqs': 26,
#     'erekle': 24,
#     # 'guliko': 26
# }

# print(names)

# print(names['guliko'])

# print(names.get('nika'))

# print(names.get('nika', 'not found'))

# names["erekle"] = 20

# print(names)

# print(len(names))

# for i in names:
#     print(i)

# for i in names:
#     print(names[i])

# for i in names:
#     print(f"{i} is {names[i]} years old")

# print(list(names.keys()))
# print(list(names.values()))

# items = list(names.items())
#
# for saxeli, asaki in items:
#     print(f"{saxeli}: {asaki}")

# names = {
#     'akaki': 20,
#     'nika': 25,
#     'elisabed': 23,
#     'guliko': 20,
#     'aleqs': 26,
#     'erekle': 24,
#     # 'guliko': 26
# }

# names.update({'erekle': 26})
# names.update({'otar': 28})
# names.setdefault('aleqs', 28)

# popped = names.pop('aleqs')
#
# last = names.popitem()
#
# print(popped)
# print(last)

# print(names)

names = ['akaki', 'nika', 'elisabed', 'guliko', 'aleqsi', 'erekle', 'ivane']
#
# n = 8
#
# my_dict = dict.fromkeys(names, n)
#
# print(my_dict)

# my_dict = {name:20 for name in names}
#
# print(my_dict)

# my_dict = {name:i+1 for i,name in enumerate(names)}
#
# print(my_dict)

# my_dict = {
#     'name': 'test',
#     1: "staesto",
#     3.14: 25,
#     False: True,
#     # [2, 4]: "test"
# }
#
# print(my_dict)

# products = {
#     "electronics": {
#         "laptops": {
#             "asus": {'price': 1500, 'quantity': 5},
#             "lenovo": {'price': 2500, 'quantity': 3},
#         },
#         "phones": {
#             "iphone": {'price': 3800, 'quantity': 5},
#             "samsung": {'price': 2300, 'quantity': 5},
#         }
#     }
# }
#
# print(products['electronics']['laptops']['asus']['price'])





















