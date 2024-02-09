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
    def serialize(self):
        return{
            "dollar_balance":self.dollar_balance,
            "doge_balance":self.doge_balance,
            "ada_balance":self.ada_balance,
            "xlm_balance":self.xlm_balance,
            "xrp_balance":self.xrp_balance,
            "bnb_balance":self.bnb_balance,
            "eth_balance":self.eth_balance,
            "btc_balance":self.btc_balance,
            "sol_balance":self.sol_balance,
            "usdt_balance":self.usdt_balance,
            "usdc_balance":self.usdc_balance
        }

class Trade(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_trades')
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    stop_loss=models.IntegerField(null=True,blank=True)
    take_profit=models.IntegerField(null=True,blank=True)
    duration=models.CharField(null=True,blank=True,max_length=20)
    closed=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Trade '

class Deposit(models.Model):
    pass

class Withdrawal(models.Model):
    pass



