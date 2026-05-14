from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Get ChromeDriver location
chromeDriverLocation = driver.service.path
print(chromeDriverLocation)

# Close the WebDriver
driver.quit()
