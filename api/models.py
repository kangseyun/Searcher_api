from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from base64 import b64encode
from datetime import datetime, timedelta

class LoginData(models.Model):
    email = models.CharField(max_length=100, blank=False)
    token = models.CharField(max_length=65)
    display_name = models.CharField(max_length=32)
    expire_time = models.DateTimeField(auto_now=False)

    def save(self, *args, **kwargs):
        if self.email:
            now_time = datetime.now()
            expire_second = 3600

            self.token = b64encode(self.email.encode()) 
            self.expire_time = now_time + timedelta(seconds = expire_second)
            
        super(LoginData, self).save(*args, **kwargs)

class Issue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created', )


class Communite(models.Model):
    subject = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    user_name = models.CharField(max_length=64, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )