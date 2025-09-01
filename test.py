import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

LT_USERNAME = os.environ.get("LT_USERNAME")
LT_ACCESS_KEY = os.environ.get("LT_ACCESS_KEY")
if not (LT_USERNAME and LT_ACCESS_KEY):
    raise SystemExit("Please set LT_USERNAME and LT_ACCESS_KEY environment variables")

hub_url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",
    "platform": "Windows 10",
    "build": "GitLab-CI",
    "name": "simple-test"
}

driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)
driver.get("https://example.com")
print("Title:", driver.title)
driver.quit()
