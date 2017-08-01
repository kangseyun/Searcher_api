from django.core.serializers import serialize
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers, mixins, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer

from googlefinance import getQuotes

import operator
import json

from api.models import Issue
from api.serializer import IssueSerializer

def issue_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        issue = Issue.objects.all()
        serializer = IssueSerializer(issue, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IssueSeriaeizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)