import imp
import selenium
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://staportal.security365.com'
driver.get(url)
driver.find_element_by_class_name('signin-box').click()
time.sleep(3)
last_tab = driver.window_handles[-1]
driver._switch_to.window(window_name=last_tab)
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('iadmin@softcamp3.onmicrosoft.com')
driver.find_element_by_id('idSIButton9').click()
time.sleep(1)
driver.find_element_by_id('i0118').send_keys('socam2021!3')
driver.find_element_by_id('idSIButton9').click()
time.sleep(1)
driver.find_element_by_id('idBtn_Back').click()
time.sleep(6)
first_tab = driver.window_handles[0]
driver.switch_to.window(window_name=first_tab )