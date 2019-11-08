class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.rating_analyzer_tab_xpath = "//span[text()='Ratings Analyzer']"
        self.comscore_tab_xpath = "//div[@aria-label='ComScore']//span[contains(text(),'ComScore')]"

    def click_ratingAnalyzerTab(self):
        self.driver.find_element_by_xpath(self.rating_analyzer_tab_xpath).click()

    def click_comscoreTab(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.comscore_tab_xpath).click()