
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time




def get_price(url:str)->int:
       driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get(url)

      # xpath of price 
       xpath_price = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]'

       time.sleep(2)
       price = driver.find_element(By.XPATH,xpath_price)
    #    print(price.text)
       return convert_price(price.text)





def convert_price(price):
    arr = price.split(',')
    num =''
    for el in arr:
         num+=el
    return int(num)
