from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fcm.utils import get_device_model
from api.models import LoginData, ConditionPermission, ConditionExpressList
from fcm.utils import get_device_model
import json
import urllib
from bs4 import BeautifulSoup

def rank_one(request):
    result = []
    result2= []

    fb = urllib.request.urlopen('http://finance.naver.com/sise/sise_rise.nhn')
    source = fb.read()
    fb.close()

    soup = BeautifulSoup(source, "html.parser")
    body = soup.findAll('table')
    t = []
    for tr in body[1].find_all('tr'):
        t.append(tr)

    for i in range(1,10):
        test = t[i].find_all('td')
        for i in test:
            if i.a:
                result.append(i.a.text)
            for obj in i.find_all("span", class_="tah p11 red01"):
                result2.append(obj.text.strip())
    obj = {"name": result, "name2": result2}
    return JsonResponse(obj, safe=False)

def rank_down(request):
    result = []
    result2= []

    fb = urllib.request.urlopen('http://finance.naver.com/sise/sise_fall.nhn')
    source = fb.read()
    fb.close()

    soup = BeautifulSoup(source, "html.parser")
    body = soup.findAll('table')
    t = []
    for tr in body[1].find_all('tr'):
        t.append(tr)

    for i in range(1,20):
        test = t[i].find_all('td')
        for i in test:
            if i.a:
                result.append(i.a.text)
            for obj in i.find_all("span", class_="tah p11 nv01"):
                result2.append(obj.text.strip())

    my_list = [x for x in result2 if x.find('%') != -1]
    obj = {"name": result, "name2": my_list}
    return JsonResponse(obj, safe=False)


def kosdaq_up(request):
    result = []
    result2= []

    fb = urllib.request.urlopen('http://finance.naver.com/sise/sise_rise.nhn?sosok=1')
    source = fb.read()
    fb.close()

    soup = BeautifulSoup(source, "html.parser")
    body = soup.findAll('table')
    t = []
    for tr in body[1].find_all('tr'):
        t.append(tr)

    for i in range(1,10):
        test = t[i].find_all('td')
        for i in test:
            if i.a:
                result.append(i.a.text)
            for obj in i.find_all("span", class_="tah p11 red01"):
                result2.append(obj.text.strip())
    obj = {"name": result, "name2": result2}
    return JsonResponse(obj, safe=False)

def kosdaq_down(request):
    result = []
    result2= []

    fb = urllib.request.urlopen('http://finance.naver.com/sise/sise_fall.nhn?sosok=1')
    source = fb.read()
    fb.close()

    soup = BeautifulSoup(source, "html.parser")
    body = soup.findAll('table')
    t = []
    for tr in body[1].find_all('tr'):
        t.append(tr)

    for i in range(1,20):
        test = t[i].find_all('td')
        for i in test:
            if i.a:
                result.append(i.a.text)
            for obj in i.find_all("span", class_="tah p11 nv01"):
                result2.append(obj.text.strip())
    my_list = [x for x in result2 if x.find('%') != -1]

    obj = {"name": result, "name2": my_list}
    return JsonResponse(obj, safe=False)

