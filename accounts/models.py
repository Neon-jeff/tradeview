from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
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
    profit=models.IntegerField(default=0,null=True,blank=True)

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
            "usdc_balance":self.usdc_balance,
            "profit":self.profit
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

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Trade '

class Deposit(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_deposit',null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    currency=models.CharField(null=True,blank=True,max_length=20)
    proof=CloudinaryField('image',blank=True,null=True)
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
    pass



