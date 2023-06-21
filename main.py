#Tracker
from track import check_price


def track():
    url = input('enter the url of the product: ')
    track_price = int(input('enter the price it should track : '))
    price = check_price(url,track_price)
    if type(price)==str:
        print("error")
    else:
        print('Yayy!!! price dropped from, ₹',track_price,' to ₹', price)
        print('You Can Save  ₹ ', track_price-price)

def main():
    track()

if __name__=='__main__':
    main()
