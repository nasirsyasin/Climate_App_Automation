import os

from Utility.web_driver_base_setup import web_driver_setup
from selenium import webdriver


def driver_access_mixpanel():
    mixpanel_url = os.getenv("MIXPANEL_URL", "https://mixpanel.com/")
    driver = web_driver_setup(mixpanel_url)
    return driver
