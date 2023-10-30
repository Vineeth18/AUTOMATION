from selenium import webdriver
import time 
from time import sleep
import os

print(os.getcwd())
#print(webdriver) 


class Instagram:

	def __init__(self,userid,pwd):

		chrome_driver_path = os.path.join(os.getcwd())

		self.browser = webdriver.Chrome(executable_path = "C:/Users/admin/AppData/Local/Programs/Python/Python38-32/Scripts/programs/chromedriver.exe")
		#self.browser = os.path.join(os.getcwd() + 'xxx' + 'yyy.exe')
		#self.browser = webdriver.Chrome() - LEAVE ARGUMENTS AS BLANK - IF CHROMEDRIVER IS IN THE PROJECT PATH

		#start_time = time.perf_counter()

		self.browser.get("https://instagram.com")

		sleep(2)

		self.browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(userid)
		self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pwd)
		self.browser.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(10)
		self.browser.implicitly_wait(5)
		self.browser.maximize_window()


Instagram('jb_vineethh','asfsdf')