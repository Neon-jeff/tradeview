from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
from .qr_code import CreateQRCode
# Create your models here.


class CopyTrader(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    win_rate=models.CharField(null=True,blank=True,max_length=200)
    wins=models.CharField(null=True,blank=True,max_length=200)
    losses=models.CharField(null=True,blank=True,max_length=200)
    profit_share=models.CharField(null=True,blank=True,max_length=200)
    copy_amount=models.IntegerField(default=0,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='copy-traders')
    followers=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{self.name} Expert Trader'




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    verified=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True,max_length=300)
    phone=models.CharField(blank=True,null=True,max_length=30)
    state=models.CharField(null=True,blank=True,max_length=50)
    country=models.CharField(blank=True,null=True,max_length=30)
    address=models.CharField(blank=True,null=True,max_length=300)
    phone_code=models.CharField(blank=True,null=True,max_length=30)
    avatar=models.ImageField(upload_to='profile',null=True,blank=True)
    dollar_balance=models.IntegerField(default=0,null=True,blank=True)
    usdt_balance=models.IntegerField(default=0,null=True,blank=True)
    btc_balance=models.IntegerField(default=0,null=True,blank=True)
    eth_balance=models.IntegerField(default=0,null=True,blank=True)
    profit=models.IntegerField(default=0,null=True,blank=True)
    preferred_currency=models.CharField(null=True,blank=True,max_length=30)
    trading_profile=models.ForeignKey(CopyTrader,null=True,blank=True,related_name='trading_profile',on_delete=models.PROTECT)
    otp=models.CharField(max_length=6,null=True,blank=True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile '
    def serialize(self):
        return{
            "dollar_balance":self.dollar_balance,
            "eth_balance":self.eth_balance,
            "btc_balance":self.btc_balance,
            "usdt_balance":self.usdt_balance,
            "profit":self.profit,
            "trading_profile_id":self.trading_profile.id if self.trading_profile!=None else 0
        }

class Trade(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_trades')
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    stop_loss=models.IntegerField(null=True,blank=True)
    take_profit=models.IntegerField(null=True,blank=True)
    duration=models.CharField(null=True,blank=True,max_length=20)
    closed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    expert_trade=models.BooleanField(default=False,null=True,blank=True)
    lost_trade=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Trade '

class Deposit(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_deposit',null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    # proof=CloudinaryField('image',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    confirmed=models.BooleanField(blank=True,null=True,default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.currency} Deposit '

    # automatically update balance
    def save(self,*args,**kwargs):
        if self.confirmed:
            self.user.profile.dollar_balance=self.user.profile.dollar_balance + self.amount
            self.user.profile.save()
        super(Deposit,self).save(*args,**kwargs)


class Withdrawal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_withdrawal',null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    confirmed=models.BooleanField(blank=True,null=True,default=False)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Withdrawal Request'
    def save(self,*args,**kwargs):
        if self.confirmed:
            self.user.profile.dollar_balance=self.user.profile.dollar_balance - self.amount
            self.user.profile.save()
        super(Withdrawal,self).save(*args,**kwargs)


class Deposit_Wallets(models.Model):
    ticker_code=models.CharField(max_length=100,null=True,blank=True)
    coin=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    image=models.URLField(max_length=200,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.image=CreateQRCode(coin=self.ticker_code,address=self.address)
        super(Deposit_Wallets, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.coin.capitalize()} Address'

# create copy trader section


