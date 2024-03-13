# fetch data from coin market cap
import requests
from pathlib import Path
import os
# constants

forex_symbols=[
    'USD','GBP','EUR','AUD','CAD','CHF','NZD'
]

Base_Dir=Path(__file__).parents[1]

path=f'{Base_Dir}\\static\\images\\forex'

image_list=os.listdir(path)
pair_list=[pair.split('.')[0] for pair in image_list]
first_currencies=sorted(list(set([pair[:3] for pair in pair_list])))
# second_currencies=[pair[3:] for pair in pair_list]
Currency_and_available_pair={

}
for leading in first_currencies:
  Currency_and_available_pair[leading]=[pair[3:] for pair in pair_list if pair[:3]==leading]
# ALGORITHM AND MOTIVATION:
"""
from the list of png image of currency pairs,
i'll create a data-structure that maps a leading currency to the
matching currency keeping in mind that im restricted
to the images available and the naming convention

test_data_structure=[
  {
    "currency-pair":First_Currency_Second_Currency,
    "image":First_Currency_Second_Currency.png,
    "rate":api_response_value
  }
]
"""

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


def Forex_Pairs():
      result={}
      url=''
      headers={
        "X-RapidAPI-Host":"exchangerate-api.p.rapidapi.com",
        "X-RapidAPI-Key":"6bee04bf0fmsh91e6a790ee2e537p152a6ajsn7ed0fcc5e5b1"
      }
      for currency in forex_symbols:
            response=requests.get(
              f'https://exchangerate-api.p.rapidapi.com/rapid/latest/{currency}',
              headers=headers
              )
            pairs=[{
              f'{currency}{x}':response.json()['rates'][x]
            } for x in second_currencies if x !=currency]
            result[currency]=pairs
      return result


def Forex_Currencies():
      result=[]
      headers={
        "X-RapidAPI-Host":"exchangerate-api.p.rapidapi.com",
        "X-RapidAPI-Key":"6bee04bf0fmsh91e6a790ee2e537p152a6ajsn7ed0fcc5e5b1"
      }
      for currency in Currency_and_available_pair.keys():
            response= requests.get(
              f'https://exchangerate-api.p.rapidapi.com/rapid/latest/{currency}',
              headers=headers
              )
            pairs=[{
              f'{currency}{x}':response.json()['rates'][x]
            } for x in Currency_and_available_pair[currency] ]
            result.extend(pairs)
      result=[{
        "currency":list(data.keys())[0],
        "rate":list(data.values())[0],
        "image":list(data.keys())[0]+'.png'
      } for data in result]
      return result

def StockData():
      pass


# print(Currency_and_available_pair)

