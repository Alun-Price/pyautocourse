import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_driver():
    """
    Set up and return a Selenium WebDriver instance configured for automated
    browsing.

    This function configures Chrome options to disable infobars, start
    maximized, disable dev shm usage, disable sandboxing, exclude automation
    switches, and disable blink features related to automation control.
    It then initializes a Chrome WebDriver with these options and navigates
    to the specified URL.

    Returns:
        webdriver.Chrome: An instance of the Chrome WebDriver.
    """
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    """calls the get_driver function"""
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys(
        "automatedautomated" + Keys.RETURN
    )
    time.sleep(2)
    driver.find_element(by="link text", value="Home").click()
    time.sleep(5)
    print(driver.current_url)


print(main())
