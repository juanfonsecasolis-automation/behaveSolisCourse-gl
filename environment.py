from hooks.DriverFactory import DriverFactory
from selenium import webdriver
from user_configs.UserConfigs import get_user_configs

def before_all(context):
    driverFactory = DriverFactory()
    browser = context.config.userdata.get("browser")
    context.user_configs = get_user_configs(context)
    context.driver = driverFactory.get_webdriver(context.user_configs['browser'])

def after_all(context):
    context.driver.quit()
