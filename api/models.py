from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from base64 import b64encode
from datetime import datetime, timedelta


class ConditionExpressList(models.Model):
    express_index = models.IntegerField(default=0)
    express_name = models.CharField(primary_key=True, max_length=64, blank=False)
    express_content = models.TextField(default='')
    
    def __str__(self):
        return self.express_name

class ConditionPermission(models.Model):
    name = models.CharField(max_length=30, default='')
    stock = models.ManyToManyField(ConditionExpressList, blank=True, verbose_name="user_permission")

    def __str__(self):
        return self.name

class InvestmentItems(models.Model):
    item_code = models.CharField(max_length=32)
    item_name = models.CharField(max_length=48, blank=False)
    item_condition = models.ForeignKey(ConditionExpressList)

    item_marketcap = models.IntegerField(blank=False, default=0)    

    item_transactions = models.IntegerField(blank=False, default=0)

    item_current_price = models.IntegerField(blank=False, default=0)
    item_high_price = models.IntegerField(blank=False, default=0)
    item_low_price = models.IntegerField(blank=False, default=0)
    item_price = models.IntegerField(blank=False, default=0)
    item_yester_price = models.IntegerField(blank=False, default=0)

    item_percentage = models.FloatField(blank=False, default=0)

    def __str__(self):
        return self.item_name

class LoginData(models.Model):
    email = models.CharField(max_length=100, blank=False)
    token = models.CharField(max_length=65)
    display_name = models.CharField(max_length=32)
    expire_time = models.DateTimeField(auto_now=False)
    permission = models.ForeignKey(ConditionPermission, verbose_name='user_permission')
    push = models.CharField(max_length=200, default='')


    def save(self, *args, **kwargs):
        if self.email:
            now_time = datetime.now()
            expire_second = 3600

            self.token = b64encode(self.email.encode()) 
            self.expire_time = now_time + timedelta(seconds = expire_second)
            
        super(LoginData, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class Issue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.subject

class Communite(models.Model):
    subject = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    user_name = models.CharField(max_length=64, null=True)
    user_email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )


    def __str__(self):
        return self.subject