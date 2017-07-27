from django.core import serializers
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render

from rest_framework import serializers, mixins, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import Communite, LoginData
from api.serializer import communitySerializer, communityJSONRenderer

from googlefinance import getQuotes

import json
import operator

def get_community(request):
    if request.method == 'GET':
        n = int(request.GET.get('n'))
        token = request.GET.get('token')

        instance = Communite.objects.all()[n] 
        login_instance = LoginData.objects.filter(token=token)[0]

        serializer = communitySerializer(instance)

        if login_instance.email == instance.user_email:
            r = communityJSONRenderer().render(serializer.data, status=True)
        else:
            r = communityJSONRenderer().render(serializer.data)

        return HttpResponse(r, content_type="application/json")


def community_list(request):
    if request.method == 'GET':
        obj = Communite.objects.all()
        serializer = communitySerializer(obj, many=True)

        return JsonResponse(serializer.data, safe=False)

def delete_community(request):
    return_data = {'status' : 'success'}

    if request.method == 'GET':
        n = int(request.GET.get('n'))
        token = request.GET.get('token')

        login_instance = LoginData.objects.filter(token = token)[0]

        if login_instance:
            instance = Communite.objects.all()[n]
            instance.delete()
        else:
            return_data['status'] = 'failed'

    return JsonResponse(return_data, safe=False)        


@csrf_exempt
def community_post(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        token = request.POST.get('token')

        user_instance = LoginData.objects.filter(token=token)[0]
        if not user_instance:
            pass  #  Show Error

        instance = Communite(subject=subject, content=content, user_email=user_instance.email, user_name=user_instance.display_name)
        instance.save()

        serializer = communitySerializer(instance)
        r = JSONRenderer().render(serializer.data)

        return HttpResponse(r, content_type="application/json")