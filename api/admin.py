from django.contrib import admin
from api.models import Issue, Communite, LoginData
# Register your models here.

admin.site.register(LoginData)
admin.site.register(Issue)
admin.site.register(Communite)