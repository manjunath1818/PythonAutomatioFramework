import allure
import moment
from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():



    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        driver.implicitly_wait(20)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
    def test_home(self):
        try:
            driver = self.driver
            driver.implicitly_wait(50)

            homepage = HomePage(driver)
            homepage.click_ratingAnalyzerTab()
            homepage.click_comscoreTab()
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.thisFunctionName()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/manjunathk/PycharmProjects/AutomatioFramework/screenshots/" + screenshotName + ".png")
            x = driver.title
            assert x == "AOS-Rating Analyzer"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)


            raise

        except:
            print("There is no exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.thisFunctionName()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        else:
            print("No exception")

        finally:
            print("I am inside finally block")




