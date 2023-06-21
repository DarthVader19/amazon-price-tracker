import requests
from bs4 import BeautifulSoup

from page import get_price

# using BeautifullSoup

import time

def extract_data(page):
    pg_soup = BeautifulSoup(page)
    try:
        #somelogic
        print(pg_soup)
        print('try logic ')
    except:
        print('erorr in data extraction')



def check_price(url,track_price=None):
    count =0
    if track_price==None :
        track_price = get_price(url) - 1

    page = requests.get(url)
    if page.status_code == 200:
        print('200 ok')
        price = get_price(url)
        while price >track_price and count <30:
            price = get_price(url)
            time.sleep(10)
            count+=1
       
        return price
    else:
        return 'error fecthing'



def main():
    url = 'https://www.amazon.in/AmazonBasics-Induction-Cooktop-1900-Watt/dp/B07YCCX789/ref=sr_1_17?keywords=induction+cooktop&qid=1687203409&sprefix=indu%2Caps%2C302&sr=8-17'

    page = check_price(url,1800)
    print(page)


if __name__=='__main__':
    main()