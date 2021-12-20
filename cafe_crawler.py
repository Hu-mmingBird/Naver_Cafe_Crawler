import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import time
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
dir_driver=chromedriver_autoinstaller.get_chrome_version().split('.')[0]
# print(dir_driver)
driver=webdriver.Chrome(THIS_FOLDER+f'/{dir_driver}/chromedriver.exe')
url='https://cafe.naver.com/tgpia/611342'
driver.get(url)
#driver.implicitly_wait(2)
driver.switch_to.frame('cafe_main')
page_source=driver.page_source
articleid=''
clubid=''
src=f'//cafe.naver.com/ca-fe/ArticleRead.nhn?articleid={articleid}&clubid={clubid}'



# soup=bs(driver.page_source,'html.parser')#전체내용이 나오는데

# driver = webdriver.Chrome(THIS_FOLDER+'/chromedriver.exe')#버전 96.0.4664.110(공식 빌드) (64비트)
# driver.switch_to_frame('cafe_main')
# iframes=driver.find_element_by_css_selector('iframe')
# for iframe in iframes:
#     print(iframe.get_attribute('name'))
