from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from fcm.utils import get_device_model

from api.models import LoginData, ConditionPermission

import json
import urllib.parse

response_data = {'status': 'token_ok', 
                'email': '',
                'token': ''}

@csrf_exempt
def login(request):  # 푸쉬 토큰 등록.
    if request.method == "POST":
        request_email = request.POST.get('userEmail')
        request_displayname = request.POST.get('userDisplayName')

        login_instance, permission_instance = [None, None]

        try:
            permission_instance = ConditionPermission.objects.all()[0]
            login_instance = LoginData.objects.filter(email=request_email)[0]
        except:
            pass

        print(permission_instance)

        if not login_instance:
            newLoginInstance = LoginData(email=request_email,
                                         display_name=request_displayname,
                                         permission=permission_instance)

            newLoginInstance.save()

            response_data['status'] = 'login_ok'
            response_data['token'] = newLoginInstance.token.decode()
        else:
            response_data['token'] = login_instance.token

        response_data['email'] = request_email

    else:
        response_data['status'] = 'error'
    
    return JsonResponse(response_data, safe=False)

def logout(request):
    if request.method == "GET":
        request_token = request.GET.get('userToken')
        instance = LoginData.objects.filter(token = request_token)

        if instance:
            instance.delete()
            response_data['status'] = 'logout_ok'

    return JsonResponse(response_data, safe=False)
        
def token_check(request):
    if request.method == "GET":
        request_token = request.GET.get('userToken')
        instance = LoginData.objects.filter(token = request_token)

        if instance:
            response_data['status'] = 'valid_token'
        else:
            response_data['status'] = 'invalid_token'

    return JsonResponse(response_data, safe=False)