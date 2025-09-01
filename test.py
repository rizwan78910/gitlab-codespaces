import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get LambdaTest credentials from CI/CD variables
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

chrome_options = Options()
for key, value in capabilities.items():
    chrome_options.set_capability(key, value)

# Selenium 4 requires 'options' instead of 'desired_capabilities'
driver = webdriver.Remote(command_executor=hub_url, options=chrome_options)

driver.get("https://example.com")
print("Title:", driver.title)
driver.quit()