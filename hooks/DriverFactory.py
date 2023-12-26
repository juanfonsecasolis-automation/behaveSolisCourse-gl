from selenium import webdriver

class DriverFactory:

    def get_webdriver(self, browser):
        if(browser == 'chrome'):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("headless")
            driver = webdriver.Chrome(chrome_options=chrome_options) 
            driver.set_page_load_timeout(20)
            driver.implicitly_wait(20)
            driver.maximize_window()
            return driver 
        else:
            raise ValueError('Unknown browser %s' % browser)