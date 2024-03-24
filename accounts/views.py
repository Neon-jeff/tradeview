from django.shortcuts import render,redirect
from .handlers import FetchCoinData,Forex_Currencies,StockData
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core import serializers
from .utils import *
from .locations import CountryData
import uuid
from django.conf import settings


# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user:
            auth_user=authenticate(username=user.username,password=password)
            if auth_user == None:
                messages.error(request,'Invalid Credentials, check password')
                return render(request,'pages/login.html')
            else:
                login(request, auth_user)
                return redirect('dashboard')
        else:
            messages.error(request,'No existing account')
            return render(request,'pages/login.html')
    return render(request,'pages/login.html',status=200)


def SignUpView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        data=request.POST
        email=data['email']
        if User.objects.filter(email=email).first() is not  None:
            return JsonResponse({"status":"failure"},safe=False)
        else:
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['email'],
            )
            user.set_password(data['password'])
            user.save()
            Profile.objects.create(
                user=user,
                country=data['country'],
                address=data['address'],
                phone_code=data['phone_code'],
                phone=f"+{data['phone_code']}{data['phone']}",
                verified=False,
                token=uuid.uuid4()

            )
            login(request,user)
            # Send welcome email to user
            SendEmail(user=user,request=request)
            messages.success(request,"Registration Successful")
            return JsonResponse({"status":"success"},safe=False)
    return render(request,'pages/register.html',{"countries":CountryData()},status=200)




def ActivateAccount(request):
    profile=Profile.objects.filter(token=request.GET['token']).first()
    if profile.verified:
        messages.success(request,'Account already verified')
        return redirect('login')
    profile.verified=True
    profile.save()
    messages.success(request,'Account successfully verified')
    return redirect('login')


def SignUpSuccessView(request):
    return render(request,'pages/register-success.html')


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Dashboard(request):
    user_profile=Profile.objects.filter(user=request.user).first()
    user_json=user_profile.serialize()
    assets={
        "crypto":FetchCoinData(),
        "forex":Forex_Currencies(),
        "stocks":StockData()
        }
    total_deposit=sum([x.amount for x in request.user.user_deposit.filter(confirmed=True)])
    return render(request,'dashboard/dashboard.html',{"assets":assets,"user":user_json,"deposit":total_deposit})

@login_required(login_url='login')
def Assets(request):
    user_profile=Profile.objects.filter(user=request.user).first()
    user_json=user_profile.serialize()
    assets=FetchCoinData()
    return render(request,'dashboard/assets.html',{"assets":assets,"user":user_json})

@login_required(login_url='login')
def Trades(request):
    assets=FetchCoinData()
    user_profile=Profile.objects.filter(user=request.user).first()
    user_json=user_profile.serialize()
    open_trades=Trade.objects.filter(user=request.user,closed=False).order_by('-id')
    closed_trades=Trade.objects.filter(user=request.user,closed=True).order_by('-id')
    if request.method=='POST':
        data=request.POST
        Trade.objects.create(
            user=request.user,
            amount=int(data['amount']),
            currency=data['currency'],
            take_profit=int(data['take_profit']),
            stop_loss=int(data['stop_loss']),
            duration=data["duration"]
        )
        request.user.profile.dollar_balance=request.user.profile.dollar_balance-int(data["amount"])
        request.user.profile.save()
        messages.success(request,"Open trade successful")
        return JsonResponse({"status":"success"},safe=False)
    return render(request,'dashboard/trades.html',{"assets":assets,"user":user_json,"open_trades":open_trades,"closed_trades":closed_trades})

def UserCoinBalance(request):
    pass

@login_required(login_url='login')
def Market(request):
    assets=FetchCoinData()
    return render(request,'dashboard/markets.html',{"assets":assets})

@login_required(login_url='login')
def CoinDetails(request):
    pass

@login_required(login_url='login')
def DepositFunds(request):
    user_deposits=Deposit.objects.filter(user=request.user)
    wallet_address=[
        {
            "name":"BTC",
            "address":"bc1qzrfrgl3724mperf2yfj6x6lz46vq4ueuekrh8h",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"
        },
                {
            "name":"ETH",
            "address":"0x1d6A91643e8eC808a631eA407549E47d1A8A95b2",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"
        },
                {
            "name":"USDC",
            "address":"0x1d6A91643e8eC808a631eA407549E47d1A8A95b2",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/3408.png"
        },
                {
            "name":"SOL",
            "address":"7UCrfvnQueCAv8CvEgLAR9D2hLUK73N8piRoTUZupRJf",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png"
        },
                {
            "name":"XRP",
            "address":"r4sB7FUqpPpQcMKDzKwWVabANJetfCoefZ",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"
        },
                {
            "name":"ADA",
            "address":"addr1q9v0ewrg6pw6rflngn7y6alu98tkreqg52tuypdcjqp405zcljux35za5xnlx38uf4mlc2whv8jq3g5hcgzm3yqr2lgqcw9nay",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"
        },
                {
            "name":"XLM",
            "address":"GAGPB22G7V7QZMDPTOK4JG256QU5QJTEOPBUGOZNPBKFTHGR3WGD6PR4",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/512.png"
        },
                {
            "name":"BNB",
            "address":"bnb1vp0xpxj00u0msy4r35dj3xv0ggmk8g7m6ujk6k",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png"
        },
                {
            "name":"DOGE",
            "address":"DLXjjitFEXdW7e2w9wFFNMdPMccPrQyY7y",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/74.png"
        }
    ]
    # def get_image(name):
    #     return
    if request.method=='POST':
        data=request.POST
        # image=request.FILES['image']
        Deposit.objects.create(
            user=request.user,
            amount=data['amount'],
            currency=data['currency'],
            # proof=image
        )
        return JsonResponse({"status":"success"},safe=False,status=200)
    return render(request,'dashboard/deposit.html',{"wallets":wallet_address,"deposits":user_deposits})

@login_required(login_url='login')
def Withdraw(request):
    wallet_address=[

                {
            "name":"ETH",
            "address":"0x1d6A91643e8eC808a631eA407549E47d1A8A95b2",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"
        },

                {
            "name":"XRP",
            "address":"r4sB7FUqpPpQcMKDzKwWVabANJetfCoefZ",
            "image":"https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"
        },

    ]
    if request.method=='POST':
        data=request.POST
        Withdrawal.objects.create(
            user=request.user,
            amount=data['amount'],
            currency=data['currency'],
        )
        return JsonResponse({"status":"success"},safe=False,status=200)

    return render(request,'dashboard/withdraw.html',{"wallets":wallet_address,'user':request.user.profile.serialize()})

def CopyTrades(request):
    return render(request,"dashboard/copy.html",{"user":request.user.profile.serialize()})


def SelectMethod(request):
    return render(request,"dashboard/select-method.html",{"user":request.user.profile.serialize()})

def PayWithBank(request):
    return render(request,"dashboard/deposit-bank.html",{"user":request.user.profile.serialize()})

def PayWithCard(request):
    return render(request,"dashboard/deposit-card.html",{"user":request.user.profile.serialize()})
