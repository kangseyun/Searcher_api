from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import LoginData

import json
import urllib.parse

response_data = [{'status': 'token_ok', 
                'email': '',
                'token': ''}]

@csrf_exempt
def login(request):
    if request.method == "GET":
        request_token = request.GET.get('user_token')
        if not LoginData.objects.filter(token = request_token):
            response_data[0]['status'] = 'token_invalid'

    elif request.method == "POST":
        response_data = [{'status': 'login_ok'}]

        print (request.body)

        request_email = request.POST.get('userEmail')
        request_displayname = request.POST.get('userDisplayName')

        instance = LoginData.objects.filter(email = request_email)

        if not instance:
            newLoginInstance = LoginData(email = request_email, display_name = request_displayname)
            newLoginInstance.save()

            response_data[0]['status'] = 'login_ok'
            response_data[0]['token'] = newLoginInstance.token.decode()
        else:
            response_data[0]['token'] = instance[0].token

        response_data[0]['email'] = request_email

    else:
        response_data[0]['status'] = 'error'
    
    return JsonResponse(response_data, safe=False)

def logout(request):
    if request.method == "GET":
        request_token = request.GET.get('userToken')
        instance = LoginData.objects.filter(token = request_token)

        if instance:
            instance.delete()
            response_data[0]['status'] = 'logout_ok'

    return JsonResponse(response_data, safe=False)
        
def token_check(request):
    if request.method == "GET":
        request_token = request.GET.get('userToken')
        instance = LoginData.objects.filter(token = request_token)

        if instance:
            response_data[0]['status'] = 'token_valid'
    
    return JsonResponse(response_data, safe=False)