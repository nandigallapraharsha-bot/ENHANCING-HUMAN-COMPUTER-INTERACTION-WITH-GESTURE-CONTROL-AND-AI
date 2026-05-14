from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class infow():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hp\Desktop\drivers\geckodriver.exe")

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))
        search_input.send_keys(query)
        search_input.submit()


