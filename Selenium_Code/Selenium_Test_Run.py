import imp
import selenium
import logging
import time
import SendMail
import chromedriver_autoinstaller

#os.path.isdir(path): //경로안에

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
logging.basicConfig(level=logging.INFO)

#헤드리스 적용 옵션
options = Options()
options.add_argument('--headless=new')

''''
#크롬드라이버 자동 설치driver
print('chromedriver_autoinstaller 실행')
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
driver_path = f'./{chrome_ver}/chromedriver'


try:
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)   
except:
    chromedriver_autoinstaller.install(True)
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
'''
#Portal 로그인
driver = webdriver.Chrome(options=options)
url = 'your test page url'
driver.get(url)
driver.implicitly_wait(10)
#MS로 로그인하기 버튼 클릭
try:
    driver.find_element(By.ID, 'ms_login').click()
except Exception as e:
    logging.error("로그인 테스트 실패" + f"\n예외가 발생했습니다: {str(e)}")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('로그인 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()    
time.sleep(3)
#MS 로그인 창 ID/PW 입력
last_tab = driver.window_handles[-1]
driver._switch_to.window(window_name=last_tab)
try:
    "사용자 계정 로그인" in driver.title
    logging.info("로그인 UI 테스트 성공")
except Exception as e:
    logging.error("로그인 UI 테스트 실패" + f"\n예외가 발생했습니다: {str(e)}")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('로그인 UI 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
time.sleep(2)    
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('your ID')
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="i0118"]').send_keys('your PW')
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()
#Portal 창으로 이동
time.sleep(3)
first_tab = driver.window_handles[0]
driver.switch_to.window(window_name=first_tab)
#테스트 성공/실패 여부 체크(로그)
time.sleep(3)
if driver.current_url == "your login page url":
    logging.info("Portal 로그인 테스트 성공")
    #SendMail.send_email('Portal 로그인 테스트 결과', '테스트 성공')
elif driver.current_url == "if URL":
    logging.error("Portal 로그인 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('Portal 로그인 테스트 결과', '테스트 실패', 'screenshot.png')
    raise
else:
    logging.error("Portal 로그인 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('Portal 로그인 테스트 결과', '테스트 실패', 'screenshot.png')
    raise
#------------------------------------------------------------------------------------------------

#Portal 메인화면
#Security365 LNB 메뉴 체크
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[3]/h2')
    logging.info("메인 화면 Security365 LNB 메뉴 체크 테스트 성공")
except Exception as e:
    logging.error("메인 화면 Security365 LNB 메뉴 체크 테스트 실패" + f"\n예외가 발생했습니다: {str(e)}")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('메인 화면 Security365 LNB 메뉴 테스트 결과', '테스트 실패'+ f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#Security365현황 체크
try:
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[3]/div/h3')
    logging.info("메인 화면 Security365 현황 메뉴 체크 테스트 성공")
except Exception as e:
    logging.error("메인 화면 Security365 현황 메뉴 체크 테스트 실패" + f"\n예외가 발생했습니다: {str(e)}")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('Security365현황 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#------------------------------------------------------------------------------------------------
        
#LNB 사용자 관리 메뉴 이동
driver.find_element_by_xpath('//*[@id="app"]/div/aside/div[1]/div/div[2]/div[2]/div').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/h1')
    logging.info("LNB 사용자 관리 메뉴 테스트 성공")
except Exception as e:
    logging.error("LNB 사용자 관리 메뉴 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 관리 메뉴 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#사용자 추가 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[1]/button[1]').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/h1')
    logging.info("LNB 사용자 추가 메뉴 테스트 성공")
except Exception as e:
    logging.error("LNB 사용자 추가 메뉴 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 추가 메뉴 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#사용자 등록(단일 사용자) 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/ul/li[1]').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/h1')
    logging.info("LNB 사용자 등록 메뉴 테스트 성공")
except Exception as e:
    logging.error("LNB 사용자 등록 메뉴 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 등록 메뉴 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
time.sleep(2)
#사용자 정보 입력//*[@id="app"]/div[4]/div/div[2]/form/div[1]/div[1]/div[2]/div/div[1]/div
try:
    driver.find_element_by_xpath('//*[@id="input-200"]').send_keys('test')
except Exception as e:
    logging.error("LNB 사용자 등록 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 등록 테스트 실패', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    #driver.quit()
    raise
try:    
    driver.find_element_by_xpath('//*[@id="input-204"]').send_keys('입니다')
except Exception as e:
    logging.error("LNB 사용자 등록 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 등록 테스트 실패', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
try:    
    driver.find_element_by_xpath('//*[@id="input-208"]').send_keys('test@.test.co')    
except Exception as e:
    logging.error("LNB 사용자 등록 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 등록 테스트 실패', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
time.sleep(1)
#완료 버튼 클릭(클릭 성공 시 성공)
try:
    element = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/button[2]/span')
    element.click()
    logging.info("LNB 사용자 등록 테스트 성공")
except Exception as e:
    logging.error("LNB 사용자 등록 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('LNB 사용자 등록 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#------------------------------------------------------------------------------------------------
time.sleep(5)
# 검색 입력 상자를 찾고 검색어를 입력합니다.
search_box = driver.find_element_by_xpath('//*[@id="input-115"]')
search_box.send_keys('test' + Keys.RETURN)
time.sleep(5)
# 페이지에서 "test@.test.co"이라는 텍스트가 있는지 확인합니다.
try:
    "test@.test.co" in driver.page_source
    logging.info("추가된 사용자 검색 테스트 성공")
except Exception as e:
    logging.error("추가된 사용자 검색 테스트 실패")
    driver.save_screenshot('screenshot.png')
    #SendMail.send_email('추가된 사용자 검색 테스트 결과', '테스트 실패' + f'\n예외가 발생했습니다: {str(e)}', 'screenshot.png')
    driver.quit()
    raise
#------------------------------------------------------------------------------------------------

