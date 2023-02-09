import imp
import selenium
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#SHIELDrive 사내 로그인
driver = webdriver.Chrome()
url = 'https://shieldrive.security365.co.kr/folderView?path=%2Fshare%2FCloud%EC%9A%B4%EC%98%81%ED%8C%80%2FSecurity%20365%20%EB%8C%80%EC%9D%91%2F0.RPATEST&fileName=2020.07.22_%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9CDRM%20%EC%9D%BC%EC%A0%95.pptx'
driver.get(url)
#MS로 로그인하기 버튼 클릭
driver.find_element_by_class_name('social-login-inner').click()
time.sleep(3)
#MS로그인 창 ID/PW 입력
last_tab = driver.window_handles[-1]
driver._switch_to.window(window_name=last_tab)
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('junyoung.kim@softcamp.co.kr')
driver.find_element_by_id('idSIButton9').click()
time.sleep(1)
driver.find_element_by_id('i0118').send_keys('softcamp2020!')
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_id('idBtn_Back').click()
time.sleep(6)
#SHIELDrive 창으로 이동
first_tab = driver.window_handles[0]
driver.switch_to.window(window_name=first_tab )
