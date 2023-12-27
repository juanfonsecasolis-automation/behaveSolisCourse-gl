from hooks.DriverFactory import DriverFactory
from selenium import webdriver
from user_configs.ConfigsManager import ConfigsManager

def before_all(context):
    context.configs_manager = ConfigsManager(context)
    driverFactory = DriverFactory(context.configs_manager)
    context.driver = driverFactory.get_webdriver()

def after_all(context):
    context.driver.quit()
