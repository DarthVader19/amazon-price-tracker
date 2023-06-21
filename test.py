import requests 
import json

url = 'https://www.amazon.in/Havells-Swing-400mm-Table-Cherry/dp/B00J5DY7RU/?_encoding=UTF8&pd_rd_w=A5vkE&content-id=amzn1.sym.4ae0d524-b52c-41b0-9993-b0d4d7f5b370&pf_rd_p=4ae0d524-b52c-41b0-9993-b0d4d7f5b370&pf_rd_r=Y2D159ZNMB7PJ565VPYY&pd_rd_wg=ztgMP&pd_rd_r=13b4d1be-0345-4ca2-8a21-11c131af85a2&ref_=pd_gw_deals_ct_t2&th=1'

api_url= 'http://localhost:5000/pricetracker'
res = requests.post(api_url,data={'url':url,'trackprice':2354})

print('response : ',json.loads(res.content))