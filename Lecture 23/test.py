import my_module, unittest

# class TestMyModule(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(my_module.add(5, 7), 12)
#         self.assertEqual(my_module.add(5, -7), -2)
#         self.assertEqual(my_module.add(-5, -7), -12)
#         self.assertNotEqual(my_module.add(5, 7), 54)
#
#     def test_sub(self):
#         self.assertEqual(my_module.sub(5, 7), -2)
#         self.assertEqual(my_module.sub(5, -7), 12)
#         self.assertEqual(my_module.sub(-5, -7), 2)
#         self.assertNotEqual(my_module.sub(5, 7), -3)
#
#     def test_mul(self):
#         self.assertEqual(my_module.mul(5, 7), 35)
#         self.assertEqual(my_module.mul(5, -7), -35)
#         self.assertEqual(my_module.mul(-5, -7), 35)
#         self.assertNotEqual(my_module.mul(5, 7), 54)
#
#     def test_div(self):
#         self.assertEqual(my_module.div(5, 2), 2.5)
#         self.assertEqual(my_module.div(-20, -10), 2)
#         self.assertEqual(my_module.div(-8, 2), -4)
#         self.assertNotEqual(my_module.div(5, 7), 54)
#
#         # self.assertRaises(ValueError, my_module.div, 5, 0)
#
#         with self.assertRaises(ValueError):
#             my_module.div(5, 0)
#
#     def test_is_even(self):
#         self.assertTrue(my_module.is_even(4))
#         self.assertFalse(my_module.is_even(5))


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = my_module.Student('John', 'Doe', 1200)
        self.student2 = my_module.Student('Walter', 'Lock', 1500)

    def test_get_full_name(self):
        self.assertEqual(self.student1.get_full_name, 'John Doe')
        self.assertEqual(self.student2.get_full_name, 'Walter Lock')

        self.student1.first_name = 'Jane'
        self.student2.last_name = 'Smith'

        self.assertEqual(self.student1.get_full_name, 'Jane Doe')
        self.assertEqual(self.student2.get_full_name, 'Walter Smith')

    def test_get_email(self):
        # print("testing get_email")
        # student1 = my_module.Student('John', 'Doe', 1200)
        # student2 = my_module.Student('Walter', 'Lock', 1500)

        self.assertEqual(self.student1.get_email('gmail.com'), 'John.Doe@gmail.com')
        self.assertEqual(self.student2.get_email('yahoo.com'), 'Walter.Lock@yahoo.com')

        self.student1.first_name = 'Jane'
        self.student2.last_name = 'Smith'

        self.assertEqual(self.student1.get_email('gmail.com'), 'Jane.Doe@gmail.com')
        self.assertEqual(self.student2.get_email('gmail.com'), 'Walter.Smith@gmail.com')


    def test_get_pay(self):
        # print("testing get_pay")
        # student1 = my_module.Student('John', 'Doe', 1200)
        # student2 = my_module.Student('Walter', 'Lock', 1500)

        self.student1.get_pay()
        self.student2.get_pay()

        self.assertEqual(self.student1.pay, 1080)
        self.assertEqual(self.student2.pay, 1350)

    # def tearDown(self):
    #     print("This is a tear down method")















if __name__ == '__main__':
    unittest.main()