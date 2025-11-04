# import csv
#
# passed = []
# failed = []
#
# with open('students.csv') as file:
#     reader = csv.DictReader(file)
#
#     for student in reader:
#         if int(student['Grade']) > 50:
#             passed.append(student)
#         else:
#             failed.append(student)
#
# headers = ['ID', 'First Name', 'Last Name', 'Grade']
#
# with open('passed.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(passed)
#
# with open('failed.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(failed)

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
#     def get_email(self, domain):
#         return f"{self.first_name}.{self.last_name}@{domain}"
#
# student1 = Student('walter', 'white', 55)
# student2 = Student('jessie', 'pinkman', 30)
#
# print(student1.get_email('gmail.com'))
# print(student2.get_email('yahoo.com'))


# class Suv:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return f"Speed is now {self.speed}"
#
#     def off_road(self):
#         return f"{self.make} {self.model} can offroading"
#
# class Motorcycle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return f"Speed is now {self.speed}"
#
#     def wheelie(self):
#         return f"{self.make} {self.model} can wheelie"

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return f"Speed is now {self.speed}"
#
#
# class Suv(Vehicle):
#
#     def __init__(self, make, model, year, clearance):
#         super().__init__(make, model, year)
#         self.clearance = clearance
#
#     def off_road(self):
#         return f"{self.make} {self.model} can offroading"
#
# class Motorcycle(Vehicle):
#     def wheelie(self):
#             return f"{self.make} {self.model} can wheelie"
#
#
# subaru = Suv('Subaru', 'Crosstrek', 2019, 200)
# kawasaki = Motorcycle('Kawasaki', 'Ninja650', 2019)
#
# print(subaru.accelerate(10))
# print(subaru.accelerate(30))
# print(subaru.accelerate(20))
# print(subaru.slow_down(15))
# print(subaru.slow_down(5))
# print(subaru.brake())
# print(subaru.off_road())

# print(kawasaki.accelerate(10))
# print(kawasaki.accelerate(30))
# print(kawasaki.accelerate(20))
# print(kawasaki.slow_down(15))
# print(kawasaki.slow_down(5))
# print(kawasaki.brake())
# print(kawasaki.wheelie())


# class Suv:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return f"Speed is now {self.speed}"
#
# class ElectricVehicle:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity
#         self.charge_level = 100
#
#     def charge(self, amount):
#         self.charge_level  = min(100, self.charge_level + amount)
#         return f"Charge level is now {self.charge_level}"
#
#     def move_electricity(self, amount):
#         self.charge_level = max(0, self.charge_level - amount)
#         return f"Charge level is now {self.charge_level}"
#
#
# class ElectricSuv(Suv, ElectricVehicle):
#     def __init__(self, make, model, year, battery_capacity):
#         Suv.__init__(self, make, model, year)
#         ElectricVehicle.__init__(self, battery_capacity)
#
#     def info(self):
#         return f"{self.make} {self.model} is a {self.year} {self.make} Suv with {self.battery_capacity} kWh battery"
#
# tesla = ElectricSuv('Tesla', 'Model X', 2019, 100)
#
# print(tesla.info())
# print(tesla.move_electricity(20))


# class Shape:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Rectangle(Shape):
#     def area(self):
#         return f"Rectangle area is {super().area()}"
#
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def area(self):
#         return f"Square area is {super().area()}"
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base, height)
#
#     def area(self):
#         return f"Triangle area is {super().area()/2}"

# rect = Rectangle(10, 20)
#
# print(rect.area())

# sq = Square(10)
#
# print(sq.area())

# tri = Triangle(10, 20)
# print(tri.area())

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @abstractmethod
    def area(self):
        return self.length * self.width

    def test(self):
        return "Test"

class Rectangle(Shape):
    def area(self):
        return f"Rectangle area is {super().area()}"

    def perimeter(self):
        return f"Rectangle perimeter is {2 * (self.length + self.width)}"

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return f"Square area is {super().area()}"

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return f"Triangle area is {super().area()/2}"

rect = Rectangle(10, 20)

print(rect.area())

sq = Square(10)

print(sq.area())

tri = Triangle(10, 20)
print(tri.area())
