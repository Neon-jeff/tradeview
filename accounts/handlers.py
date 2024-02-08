# fetch data from coin market cap

import requests

def FetchCoinData():
    result=[]
    key='a3fdb01c-103d-45fa-9f7f-eafd22a6da4d'
    response=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=50",headers={
        "X-CMC_PRO_API_KEY": key,
      })
    # print(response.json()["data"])
    for i in response.json()["data"]:
        x={}
        x["name"]=i["name"]
        x["symbol"]=i["symbol"]
        x["price"]=round(float(i["quote"]["USD"]["price"]),2)
        x["image"]=f'https://s2.coinmarketcap.com/static/img/coins/64x64/{i["id"]}.png'
        result.append(x)
    return result
