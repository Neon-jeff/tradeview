from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    verified=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True,max_length=300)
    avatar=models.ImageField(upload_to='profile',null=True,blank=True)
    dollar_balance=models.IntegerField(default=0,null=True,blank=True)
    usdt_balance=models.IntegerField(default=0,null=True,blank=True)
    btc_balance=models.IntegerField(default=0,null=True,blank=True)
    xlm_balance=models.IntegerField(default=0,null=True,blank=True)
    eth_balance=models.IntegerField(default=0,null=True,blank=True)
    usdc_balance=models.IntegerField(default=0,null=True,blank=True)
    xrp_balance=models.IntegerField(default=0,null=True,blank=True)
    doge_balance=models.IntegerField(default=0,null=True,blank=True)
    bnb_balance=models.IntegerField(default=0,null=True,blank=True)
    sol_balance=models.IntegerField(default=0,null=True,blank=True)
    ada_balance=models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile '

class Trade(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_trades')
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    stop_loss=models.IntegerField(null=True,blank=True)
    take_profit=models.IntegerField(null=True,blank=True)
    duration=models.CharField(null=True,blank=True,max_length=20)
    closed=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile '

class Deposit(models.Model):
    pass

class Withdrawal(models.Model):
    pass



