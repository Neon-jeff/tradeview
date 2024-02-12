from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView,name='login'),
    path('sign-up/',SignUpView,name='sign-up'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('assets/',Assets,name='assets'),
    path('trades/',Trades,name='trades'),
    path('markets/',Market,name='markets'),
    path('deposit/',DepositFunds,name='deposits'),
    path('withdraw/',Withdraw,name='withdraws'),
    path('copy/',CopyTrades,name='withdraws'),
    path('logout/',Logout,name='logout')
]
