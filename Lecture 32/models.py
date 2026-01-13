from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.shop
products = db.products

# data = [
#   {"title": "Laptop", "price": 2500, "quantity": 5, "is_available": True},
#   {"title": "Smartphone", "price": 1200, "quantity": 0, "is_available": False},
#   {"title": "Headphones", "price": 150, "quantity": 20, "is_available": True},
#   {"title": "Book: Python Basics", "price": 50, "quantity": 15, "is_available": True},
#   {"title": "Monitor", "price": 600, "quantity": 0, "is_available": False},
#   {"title": "Keyboard", "price": 100, "quantity": 10, "is_available": True},
#   {"title": "Mouse", "price": 80, "quantity": 0, "is_available": False},
#   {"title": "Chair", "price": 300, "quantity": 7, "is_available": True},
#   {"title": "Desk Lamp", "price": 70, "quantity": 12, "is_available": True},
#   {"title": "USB Drive 64GB", "price": 40, "quantity": 0, "is_available": False},
#   {"title": "Gaming Console", "price": 450, "quantity": 8, "is_available": True},
#   {"title": "Wireless Charger", "price": 35, "quantity": 0, "is_available": False},
#   {"title": "Bluetooth Speaker", "price": 120, "quantity": 25, "is_available": True},
#   {"title": "External Hard Drive 1TB", "price": 90, "quantity": 5, "is_available": True},
#   {"title": "Smartwatch", "price": 200, "quantity": 0, "is_available": False},
#   {"title": "E-book Reader", "price": 180, "quantity": 10, "is_available": True},
#   {"title": "Desk Organizer", "price": 25, "quantity": 15, "is_available": True},
#   {"title": "HD Webcam", "price": 75, "quantity": 0, "is_available": False},
#   {"title": "Portable Projector", "price": 350, "quantity": 3, "is_available": True},
#   {"title": "Noise Cancelling Headphones", "price": 300, "quantity": 0, "is_available": False}
# ]
#
# products.insert_many(data)