from accounts.handlers import FetchCoinData,Forex_Currencies,StockData
from django.shortcuts import render


def HomePage(request):
    return render(request,'pages/home.html')
    # return render(request,'pages/homepage.html',{'forex':Forex_Currencies,"crypto":FetchCoinData,'stocks':StockData})

def NewHome(request):
    return render(request,'pages/homepage.html',{'forex':Forex_Currencies,"crypto":FetchCoinData,'stocks':StockData}) 