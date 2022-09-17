# pages/views.py
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import ast
from time import time
import datetime
from django.db.models import Sum
import json
import pickle
import random
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = 'home.html'

def live(request):
    d = SensorData.objects.all()[0]
    args = {'heart_rate': d.heart_rate, 'body_temp': d.body_temp, 'date': d.date, 'ts': d.ts}
    return JsonResponse(args)

def update_live(request):
    heart_rate = request.GET["heart_rate"]
    body_temp = request.GET["body_temp"]
    ts = int(time())

    # to_update = TestModel.objects.filter(id=2).update(name='updated_name', key=new_key)
    SensorData.objects.filter(id=1).update(heart_rate=heart_rate, body_temp=body_temp, ts=ts)

    return JsonResponse(request.GET)

def l(request):
    return HttpResponse("return this string")
