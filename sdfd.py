
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless 모드 활성화

# # Chrome 브라우저 실행
browser = webdriver.Chrome()

# 웹 페이지 열
browser.get("https://www.foodnews.co.kr/")

#sch-btns 클래스를 가진 요소 찾기
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "sch-btns"))
)
element.click()

# 검색 입력란 찾기
search_input = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.ID, "search"))
)

# 사용자로부터 음식 항목 입력 받기
food_item = input("크롤링할 음식을 입력하세요: ")

# 입력한 음식 항목을 검색 입력란에 넣기
search_input.send_keys(food_item)

# 검색 버튼 클릭 (선택 사항)
submit_button = browser.find_element(By.XPATH, "//button[@title='검색' and not(@onclick)]")
submit_button.click()  # 검색 버튼 클릭

# browser.quit()  # 필요할 때 주석을 해제하여 브라우저를 닫습니다.
