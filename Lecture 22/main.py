# Single Responsibility Principle
# Bad Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Generated - {self.data}"
#
#     def write_report(self, filename):
#         with open(filename, "w") as f:
#             f.write(self.generate_report())
#
# report = Report("This is report")

# Good Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Generated - {self.data}"
#
# class ReportWriter:
#     @staticmethod
#     def write_to_file(report:Report, filename):
#         with open(filename, "w") as file:
#             file.write(report.generate_report())
#
# report = Report([1, 2, 3, 4, 5])
# rw = ReportWriter()
#
# rw.write_to_file(report, 'report.txt')


# Open/Close Principle
# Bad example

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def get_discount(self, discount_type):
#         if discount_type == 'VIP':
#             return self.price * 0.9
#         elif discount_type == 'VIP+':
#             return self.price * 0.8
#         else:
#             return self.price


# Good Example

# from abc import ABC, abstractmethod
#
# class Discount(ABC):
#     def __init__(self, price):
#         self.price = price
#
#     @abstractmethod
#     def get_discount(self):
#         pass
#
# class VIPDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.9
#
# class VIPPlusDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.8
#
# class SuperVipDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.7


# Liskov Substitution Principle
# Bad Example

# class Bird:
#     @staticmethod
#     def fly():
#         return "I can fly"
#
#     @staticmethod
#     def eat():
#         return "I can eat"
#
# class Sparrow(Bird):
#     @staticmethod
#     def eat():
#         return "I am sparrow and I can eat"
#
#     @staticmethod
#     def fly():
#         return "I am sparrow and I can fly"
#
# class Penguin(Bird):
#     @staticmethod
#     def eat():
#         return "I am penguin and I can eat"
#
#     @staticmethod
#     def fly():
#         raise Exception("I am penguin and I can't fly")


# Good Example

# class Bird:
#     @staticmethod
#     def eat():
#         return "I can eat"
#
#     @staticmethod
#     def move():
#         return "I can move"
#
# class FlyingBird(Bird):
#     @staticmethod
#     def fly():
#         return "I can fly"
#
# class SwimmingBird(Bird):
#     @staticmethod
#     def swim():
#         return "I can swim"
#
# class Penguin(SwimmingBird):
#     pass
#
# class Sparrow(FlyingBird):
#     pass


# Interface Segregation Principle
# Bad Example

# class Worker:
#     def work(self):
#         pass
#
#     def eat(self):
#         pass
#
# class Manager(Worker):
#     def work(self):
#         return "I can work"
#
#     def eat(self):
#         return "I can eat"
#
# class Robot(Worker):
#     def work(self):
#         return "I can work"
#
#     def charge(self):
#         return "I can charge"


# from abc import ABC, abstractmethod
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Chargeable(ABC):
#     @abstractmethod
#     def charge(self):
#         pass
#
#
# class Manager(Workable, Eatable):
#     def work(self):
#         return "I can work"
#
#     def eat(self):
#         return "I can eat"
#
#
# class Robot(Workable, Chargeable):
#     def work(self):
#         return "I can work"
#
#     def charge(self):
#         return "I can charge"



# Dependency Inversion Principle
# Bad Example


# class MySQLDatabase:
#     @staticmethod
#     def connect():
#         return "Connected to MySQL database"
#
# class Application:
#     def __init__(self):
#         self.database = MySQLDatabase()
#
#     def run(self):
#         return self.database.connect()
#
# app = Application()
#
# print(app.run())

# Good Example

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySqlDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database"

class PostgresqlDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL Database"

class OracleDatabase(Database):
    def connect(self):
        return "Connected to Oracle Database"

class MSSQL(Database):
    def connect(self):
        return "Connected to MSSQL Database"

class Application:
    def __init__(self, db:Database):
        self.db = db

    def run(self):
        return self.db.connect()

app = Application(MySqlDatabase())
app1 = Application(PostgresqlDatabase())
app2 = Application(OracleDatabase())

print(app.run())
print(app1.run())
print(app2.run())
























