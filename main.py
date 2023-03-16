import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/1ncVvKE1S31FOLzc7fFouRs9KSGA_aaTAqBPpt5rUbgQ/edit'
s = Service("C:\development2\chromedriver.exe")

URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
URL_3 = 'https://www.zillow.com/'
URL_2 = 'https://pytutorial.com/find-elements-by-id-python-beautifulsoup/'
content = requests.get(url=URL, headers={'Accept-Language': 'he,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'})  # href
data = content.text.encode(encoding="utf-8", errors="strict")
soup = BeautifulSoup(data, "html.parser")
my_links2 = soup.find_all("a", attrs={'class': 'property-card-link'}, recursive=True)
rental_price = soup.find_all('span', attrs={'data-test': 'property-card-price'}, recursive=True)

link_list = []
addr_list = []
price_list = []
i = 0
for link in my_links2:
    addr_list.append(link.get_text())
    link_list.append(link.get('href'))

for price in rental_price:
    price_list.append(price.get_text())

for i in range(4):
    print(addr_list[i])
    print(link_list[i])
    print(price_list[i])
    i+=1

# TODO SEND DETAILS TO FORM BY THIS LINK-->> https://docs.google.com/forms/d/1ncVvKE1S31FOLzc7fFouRs9KSGA_aaTAqBPpt5rUbgQ/edit
driver = webdriver.Chrome(service=s)
# @driver.get('https://docs.google.com/forms/d/1ncVvKE1S31FOLzc7fFouRs9KSGA_aaTAqBPpt5rUbgQ/edit')
driver.get('https://docs.google.com/forms/d/1A5f8Plws4hiZc5gA5bn0eWFh14uirDTk8qPVQClGvbI/edit')
driver.maximize_window()
driver.implicitly_wait(12)

# TODO LOCATE INPUT TEXT FIELDS  (addr price link) and  Pass through the lists
for i in range(len(addr_list)):
    addr_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr_input.send_keys(addr_list[i])
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[i])
    ui.WebDriverWait(driver, 11).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div['
                                                                             '1]/div[1]/div'))).click()
    second_page = driver.find_element(By.TAG_NAME, 'a').click()

    time.sleep(3)


#SHEET ADDRIS ====https://docs.google.com/spreadsheets/d/1Fz3Gi9H7gKSv1LHmWjQSLs7q0_7rMwaCmjP2Jf5JpF8/edit?resourcekey#gid=846448125






# TODO CLICK SECOND PAGE BACK TO EMPTY FORM AND SEND  NEW RENT OFFER

# /html/body/div[1]/div[2]/div[1]/div/div[4]/a

time.sleep(22)
print("mission completed")

# for div in soup.find_all('div', class_='search-page-list-header'):
#     print(div)
# print(div.find('a')['href'])
# print(div.find('a').contents[0])
# print(div.find('img')['src'])
