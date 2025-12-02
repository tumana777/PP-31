
# class MyError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)
#
# def test(a):
#     if a == 5:
#         raise MyError("5-is gadacema ar sheidzleba")
#
# print(test(5))

# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     if b == 0:
#         raise ValueError("Second number cannot be zero")
#     return a / b
#
# def is_even(n):
#     return n % 2 == 0

# if __name__ == "__main__":
#     print(div(5, 0))



class Student:
    discount = 0.9

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self, domain):
        return f"{self.first_name}.{self.last_name}@{domain}"

    def get_pay(self):
        self.pay *= self.discount
























