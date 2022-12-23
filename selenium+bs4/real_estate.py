from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv

#from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
#chrome to stay open
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)			
driver.get('https://www.pararius.com/apartments/amsterdam?ac=1')

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')
lists = soup.find_all('section', class_="listing-search-item")

csv_file = open('housing.csv', 'w', encoding='utf8', newline='')
csv_writer = csv.writer(csv_file)
header = ['Title', 'Location', 'Price', 'Area']
csv_writer.writerow(header)

for list in lists:
    title = list.find('a', class_="listing-search-item__link--title").text.strip()
    location = list.find('div', class_="listing-search-item__sub-title").text.strip()
    price = list.find('div', class_="listing-search-item__price").text.strip()
    area = list.find('li', class_="illustrated-features__item--surface-area").text.strip()
    info = [title, location, price, area]
    csv_writer.writerow(info)
	
    
    

    
    
    
   