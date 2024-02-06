import time

from selenium import webdriver


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
    driver.get("http://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    """calls the get_driver function"""
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]/div")
    return clean_text(element.text)


print(main())
print(main())
