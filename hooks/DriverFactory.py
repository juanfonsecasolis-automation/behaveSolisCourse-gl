from selenium import webdriver

class DriverFactory:

    configs_manager = None

    def __init__(self, configs_manager):
        self.configs_manager = configs_manager

    def get_webdriver(self):
        if(self.configs_manager.browser_name == 'chrome'):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("headless")
            driver = webdriver.Chrome(chrome_options=chrome_options) 
            driver.set_page_load_timeout(self.configs_manager.page_load_timeout)
            driver.implicitly_wait(self.configs_manager.implicitly_wait)
            driver.maximize_window()
            return driver 
        else:
            raise ValueError('Unknown browser %s' % browser)