class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.product_tab_xpath = "//span[contains(text(),'Product')]"
        self.All_Products_xpath = "//div[contains(text(),'All Products')]"

    def click_productTab(self):
        self.driver.find_element_by_xpath(self.product_tab_xpath).click()

    def click_allProductTab(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.All_Products_xpath).click()