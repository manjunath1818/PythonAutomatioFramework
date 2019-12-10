import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window();

    def test_search1(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step -Manju")
        #self.driver.find_element_by_name("hplogo").click()
        self.driver.find_element_by_name("btnk").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Google")

    def test_search2(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("MANJU manjax manju")
        #self.driver.find_element_by_name("hplogo").click()
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Google")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
