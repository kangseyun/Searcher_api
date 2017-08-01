from django.core.serializers import serialize
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import serializers, mixins, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer

from googlefinance import getQuotes

import operator
import json
import sys


def kospi(request):
        return HttpResponse(json.dumps(getQuotes('KOSPI'), indent=2), content_type="application/json")

def kosdaq(request):
        return HttpResponse(json.dumps(getQuotes('KOSDAQ'), indent=2), content_type="application/json")

def nasdaq(request):
        return HttpResponse(json.dumps(getQuotes('.IXIC'), indent=2), content_type="application/json")

def dji(request):
        return HttpResponse(json.dumps(getQuotes('.DJI'), indent=2), content_type="application/json")
