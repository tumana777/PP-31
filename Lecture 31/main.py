from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')

client = MongoClient('localhost', 27017)

# print(client.list_database_names())

db = client['PP-31']

# print(db.list_collection_names())

students = db['students']

# print(students.count_documents({}))
# print(students.count_documents({'first_name': 'Guliko'}))

# student1 = {
#     'first_name': 'Elisabed',
#     'last_name': 'Gugushvili',
#     'age': 18
# }
#
# students.insert_one(student1)


# students_list = [
#     {'first_name': 'Erekle', 'last_name': 'DarchiaShvili', 'age': 18},
#     {'first_name': 'John', 'last_name': 'Doe', 'age': 25},
#     {'first_name': 'Jane', 'last_name': 'Smith', 'age': 30},
#     {'first_name': 'Walter', 'last_name': 'Lock', 'age': 25, 'course': 'Python'}
# ]
#
# students.insert_many(students_list)

# print(students.find_one())

# for student in students.find():
#     print(student)

# for student in students.find({"first_name": "Guliko"}):
#     print(student)

# for student in students.find({"sakheli": "Guliko"}):
#     print(student)

# for student in students.find({"age": 25}):
#     print(student)

# for student in students.find({"age": {"$gt": 25}}):
#     print(student)

# for student in students.find({"age": {"$gte": 25}}):
#     print(student)

# for student in students.find({"age": {"$lt": 25}}):
#     print(student)

# for student in students.find({"age": {"$lte": 25}}):
#     print(student)


# for student in students.find({"age": {"$gt": 20, "$lt": 34}}):
#     print(student)


# for student in students.find({"age": {"$in": [20, 25, 30]}}):
#     print(student)

# for student in students.find({"first_name": {"$in": ['Guliko', 'Erekle']}}):
#     print(student)

# for student in students.find({"$or": [{"first_name": "Guliko"}, {"name": "nika"}]}):
#     print(student)

# for student in students.find({"$and": [{"first_name": "Guliko"}, {"last_name": "Kitoshvili"}]}):
#     print(student)

# for student in students.find({"$and": [{"first_name": "Walter"}, {"age": 27}]}):
#     print(student)

# for student in students.find({"first_name": "Walter", "age": 27}):
#     print(student)

# for student in students.find({"first_name": "Walter"}, {"last_name": 27}):
#     print(student)

# for student in students.find({"age": {"$ne": 27}}):
#     print(student)

# students.update_one({"first_name": "Guliko"}, {"$set": {"age": 31, "course": "Python"}})

# students.update_many({"first_name": "Guliko"}, {"$set": {"age": 32, "course": "Docker"}})

# students.update_many({}, {"$set": {"info": "I am a student", "course": "Python"}})

# students.delete_one({"first_name": "Walter"}

# students.delete_many({"age": {"$gt": 20, "$lt": 34}})

# students.delete_many({})

students.drop()