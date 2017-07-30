from django.contrib import admin
from api.models import Issue, Communite, LoginData, ConditionPermission
# Register your models here.

admin.site.register(ConditionPermission)
admin.site.register(LoginData)
admin.site.register(Issue)
admin.site.register(Communite)