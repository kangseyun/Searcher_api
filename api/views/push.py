from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fcm.utils import get_device_model
from api.models import LoginData, ConditionPermission, ConditionExpressList
from fcm.utils import get_device_model
import json
import urllib.parse


@csrf_exempt
def pushToken(request):
    response_data = {'status': 0}
    if request.method == "POST":
        email = request.POST.get('email')
        token = request.POST.get('userToken')
        obj = LoginData.objects.filter(email=email).update(push=token)
    
    response_data['status'] = 1
    return JsonResponse(response_data, safe=False)


def fcm_push(request):
    response_data = {'status': 0}
    Device = get_device_model()

    if request.method == "GET":
        condition = request.GET.get('condition')
        code = request.GET.get('code')
        
        list_obj = ConditionExpressList.objects.filter(express_index=condition)
        result = ConditionPermission.objects.all()
        t = ""
        for i in result:
            obj = LoginData.objects.filter(permission=i)
            for send in obj:
                my_phone = Device.objects.get(reg_id=send.push)
                my_phone.send_message({'message':'my test message'}, collapse_key='something')



    response_data['status'] = 1
    return JsonResponse(response_data, safe=False)
