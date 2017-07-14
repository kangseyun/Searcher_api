from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, mixins, generics, status
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
import json
from django.core.serializers import serialize
import operator
from googlefinance import getQuotes
from django.core import serializers


def kospi(request):
        return HttpResponse(json.dumps(getQuotes('KOSPI'), indent=2), content_type="application/json")

def kosdaq(request):
        return HttpResponse(json.dumps(getQuotes('KOSDAQ'), indent=2), content_type="application/json")

def nasdaq(request):
        return HttpResponse(json.dumps(getQuotes('NASDAQ'), indent=2), content_type="application/json")

def dji(request):
        return HttpResponse(json.dumps(getQuotes('.DJI'), indent=2), content_type="application/json")
