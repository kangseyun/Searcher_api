from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from fcm.utils import get_device_model

from api.models import LoginData, ConditionPermission, ConditionExpressList

import json
import urllib.parse

response_data = {'status': 0}

@csrf_exempt
def pushToken(request):
    if request.method == "POST":
        email = request.POST.get('userEmail')
        push_token = request.POST.get('userToken')

        Device = get_device_model()
        push_instance = None

        #obj = LoginData.objects.filter(email=email).update(push=token)
        try:
            login_instance = LoginData.objects.filter(email=email)[0]
            push_instance = Device.objects.filter(user=login_instance)[0]
        except:
            pass

        if (login_instance.push or login_instance.push != "no") and push_token != "no":
            login_instance.push = push_token
            login_instance.save()

        if push_instance is None and login_instance:
            Device(user=login_instance,
                   dev_id=login_instance.token,
                   reg_id=login_instance.push).save()
            

    response_data['status'] = 1
    return JsonResponse(response_data, safe=False)


def fcm_push(request):
    response_data = {'status': 0}
    Device = get_device_model()

    if request.method == "GET":
        condition_index = request.GET.get('condition_index')
        item_name = request.GET.get('item_name')
        item_price = request.GET.get('item_price')
        push_type = request.GET.get('status')
        
        list_instance = ConditionExpressList.objects.filter(express_index=condition_index)
        permission_list = ConditionPermission.objects.all()

        for perm in permission_list:
            users = LoginData.objects.filter(permission=perm)

            for user in users:
                user_device = Device.objects.filter(user=user)[0]
                message = str()

                if push_type == '1':
                    message = '{} 주식이 조건식 {} 번 에 편입되었습니다. (가격 : {})'.format(item_name,
                                                                                          condition_index,
                                                                                          item_price)
                else:
                    message = '{} 주식이 조건식 {} 번 에서 이탈 하였습니다. (가격 : {})'.format(item_name, 
                                                                                             condition_index,
                                                                                             item_price)

                user_device.send_message({'message':message}, collapse_key='something')


    response_data['status'] = 1
    return JsonResponse(response_data, safe=False)