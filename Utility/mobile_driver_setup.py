import os
from pathlib import Path

from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.common import AppiumOptions


class AppiumDriverSingleton:
    _instance = None

    def __init__(self):
        self.driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppiumDriverSingleton, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance

    @staticmethod
    def create_driver():
        capabilities = {
            "platformName": "android",
            "appium:deviceName": "3f8b7a18",
            "appium:app": os.getenv("APP_PATH", str(Path.cwd() / "Resources" / "app.apk")),
            "appium:automationName": "UiAutomator2",
            "skipDeviceInitialization": True,
            "skipServerInstallation": True,
            "dontStopAppOnReset": True,
            "fullReset": False,
            "noReset": True
        }

        appium_server = 'http://localhost:4723/wd/hub'
        try:
            driver = webdriver.Remote(appium_server, options=AppiumOptions().load_capabilities(capabilities))
            driver.implicitly_wait(10)  # Adjust the wait time as needed
            return driver
        except WebDriverException as e:
            print(f"An error occurred while creating the driver: {e}")
            return None  # Return None in case of failure

    @property
    def get_driver(self):
        if not self.driver:
            self.driver = self.create_driver()
        return self.driver
