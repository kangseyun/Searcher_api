from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer

from api.models import ConditionExpressList, InvestmentItems, LoginData
from api.serializer import ConditionSerializer, ConditionItemsSerializer, ConditionItemSerializer

def get_conditionlist(request):
    if request.method == "GET":
        user = request.GET.get('user')
        print(user)
        instance = LoginData.objects.filter(email = user)
        obj = instance[0].ConditionPermission

        print(obj.name)
        
        obj = ConditionExpressList.objects.all()
        serializer = ConditionSerializer(obj, many=True)
        r = JSONRenderer().render(serializer.data)

    return HttpResponse(r, content_type='application/json')


def get_condition_items(request):
    if request.method == "GET":
        try:
            index = int(request.GET.get('n'))
        except:  # not pass index
            pass

        instance = ConditionExpressList.objects.filter(express_index=index)[0]
        if not instance:  # invalid index
            pass

        instance = InvestmentItems.objects.filter(item_condition=instance)
        serializer = ConditionItemsSerializer(instance, many=True)

        r = JSONRenderer().render(serializer.data)
        return HttpResponse(r, content_type='application/json')

def get_condition_item(request):
    if request.method == "GET":
        try:
            item_code = request.GET.get('code')
        except:
            pass

        instance = InvestmentItems.objects.filter(item_code=item_code)[0]
        serializer = ConditionItemSerializer(instance)

        r = JSONRenderer().render(serializer.data)
        return HttpResponse(r, content_type='application/json')