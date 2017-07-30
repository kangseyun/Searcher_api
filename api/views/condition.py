from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer

from api.models import ConditionExpressList, InvestmentItems 
from api.serializer import ConditionSerializer, ConditionItemSerializer

def get_conditionlist(request):
    serializer = ConditionSerializer(ConditionExpressList.objects.all(), many=True)
    r = JSONRenderer().render(serializer.data)

    return HttpResponse(r, content_type='application/json')

def get_condition_item(request):
    if request.method == "GET":
        try:
            index = int(request.GET.get('n'))
        except:  # not pass index
            pass

        instance = ConditionExpressList.objects.filter(express_index=index)[0]
        if not instance:  # invalid index
            pass

        instance = InvestmentItems.objects.filter(item_condition=instance)
        serializer = ConditionItemSerializer(instance, many=True)

        r = JSONRenderer().render(serializer.data)
        return HttpResponse(r, content_type='application/json')