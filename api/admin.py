from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Issue, Communite, LoginData, ConditionPermission, InvestmentItems, ConditionExpressList

class Test(admin.ModelAdmin):
    filter_horizontal = ('stock', )


admin.site.register(InvestmentItems)
admin.site.register(ConditionPermission, Test)
admin.site.register(ConditionExpressList)
admin.site.register(LoginData)
admin.site.register(Issue)
admin.site.register(Communite)