#Tracker
from track import check_price,price_by_bs4



def track_v2(url='',track_price=0,auto=True):
    if auto:
      url = input('enter the url of the product: ')
      track_price = int(input('enter the price it should track : '))
    price = price_by_bs4(url,track_price)
    data={}
    if type(price)==str:
        print("error")
        data['error']=True
        data['price']= 0
    else:
        if auto:
          print('Yayy!!! price dropped from, ₹',track_price,' to ₹', price)
          print('You Can Save  ₹ ', track_price-price)
        data['error'] = False
        data['price'] = price
        data['trackprice'] = track_price

    return data

def track():
    url = input('enter the url of the product: ')
    track_price = int(input('enter the price it should track : '))
    price = check_price(url,track_price)
    if type(price)==str:
        print("error")
    else:
        print('Yayy!!! price dropped from, ₹',track_price,' to ₹', price)
        print('You Can Save  ₹ ', track_price-price)

def test():
    # track()
    # data = track_v2()
    # print(data)
    pass

if __name__=='__main__':
    test()
