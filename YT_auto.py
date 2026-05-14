from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class music():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hp\Desktop\drivers\geckodriver.exe")

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[2]')
        video.click()  # Click on the video to play it



