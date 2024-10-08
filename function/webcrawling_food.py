# function/food_search.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from function.save_food import FoodHandler  # FoodHandler import


def food_search_function():
    file_name = "임베디드_음식.xlsx"

    # 검색어 입력 받기
    food_query = input("음식 입력: ")

    food_handler = FoodHandler(file_name)
    food_handler.load_or_create()

    food_handler.add_materials(food_query)
    food_handler.save()

    # 크롬 드라이버 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # UI 없이 실행
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    path = "C:\\Users\\user\\Desktop\\Embed\\chromedriver\\chromedriver-win64\\chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 네이버 뉴스 검색 URL
    base_url = "https://search.naver.com/search.naver?where=news&query="
    search_url = base_url + food_query

    # 검색 페이지 열기
    driver.get(search_url)
    time.sleep(3)  # 페이지 로드 대기

    # 페이지 소스를 BeautifulSoup으로 파싱
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 검색 결과에서 제목과 내용 가져오기
    items = soup.select(".news_tit")  # 뉴스 제목 선택
    contents = soup.select(".api_txt_lines")  # 뉴스 내용 선택

    # 검색 결과 출력
    print("\n뉴스 제목과 내용:\n")
    for title, content in zip(items, contents):
        print(f"제목: {title.text}")
        print(f"내용: {content.text}\n")

    driver.quit()
