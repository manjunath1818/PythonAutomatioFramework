import unittest
import pytest
from selenium import webdriver
import HtmlTestRunner

@pytest.mark.usefixtures("test_setup")
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window();

    def test_search1(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_xpath("//img[@id='hplogo']").click()
        self.driver.find_element_by_xpath("(//input[@value='Google Search'])[2]").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Automation step by step - Google Search")

    def test_search2(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("manju")
        self.driver.find_element_by_xpath("//img[@id='hplogo']").click()
        self.driver.find_element_by_xpath("(//input[@value='Google Search'])[2]").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "manju - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/manjunathk/PycharmProjects/AutomatioFramework/reports'),verbosity=2)

