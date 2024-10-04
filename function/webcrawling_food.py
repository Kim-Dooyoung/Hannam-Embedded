from selenium import webdriver

browser = webdriver.Chrome()  # 크롬 실행
# browser.minimize_window() 

url = 'https://www.foodnews.co.kr/news/articleList.html'
browser.get(url)
