import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("this will run once before all the method")

    @classmethod
    def tearDownClass(cls):
        print("this will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
         print("This will run after every method")

    def test_add(self):
        self.assertEqual(Example.add(self,10,20),30)
        self.assertEqual(Example.add(self, 22, 20), 42)

    def test_sub(self):
        result1 = Example.sub(self,20,30)
        self.assertEqual(result1,-10)


if __name__ == '__main__':
    unittest.main()
# to comment ctrl and forward slash