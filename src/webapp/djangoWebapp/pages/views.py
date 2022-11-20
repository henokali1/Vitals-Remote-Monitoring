# pages/views.py
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import ast
from time import mktime as mktime
# import time as tm
from time import time
import datetime
from django.db.models import Sum
import json
import pickle
import random
from django.http import HttpResponse


ip_exp_sec = 60

# Alert Thresholds
heart_rate_alert_threshold = 100
body_temp_alert_threshold = 38


class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        d = SensorData.objects.all()[0]
        return {"ecg": d.ecg}

def live(request):
    d = SensorData.objects.all()[0]
    alert = False
    if(int(d.heart_rate) > heart_rate_alert_threshold) or (int(d.body_temp) > body_temp_alert_threshold):
        alert = True
    args = {'heart_rate': d.heart_rate, 'body_temp': d.body_temp, 'date': d.date, 'ts': d.ts, 'ecg': d.ecg, 'ecg_connected': d.ecg_connected, 'alert': alert}
    return JsonResponse(args)

def update_live(request):
    heart_rate = request.GET["heart_rate"]
    body_temp = request.GET["body_temp"]
    ecg = request.GET["ecg"]
    patient_id = request.GET["patient_id"]
    ecg_connected = ecg != "!"
    print(ecg, ecg_connected)
    ts = int(time())

    # to_update = TestModel.objects.filter(id=2).update(name='updated_name', key=new_key)
    SensorData.objects.filter(id=1).update(heart_rate=heart_rate, body_temp=body_temp, ecg_connected=ecg_connected, ts=ts)
    if ((heart_rate != '0.0') or (body_temp != '0.0')):
        # Save to HistoricalData
        HistoricalData(
            heart_rate=heart_rate,
            body_temp = body_temp,
            ts = int(time()),
            patient_id = patient_id,
        ).save()

    return JsonResponse(request.GET)

def vid(request):
	return render(request, 'pages/vid.html')

def l(request):
    return HttpResponse("return this string")

def save_ip(request):
    ip = request.GET["ip"]
    Ip.objects.filter(id=1).update(
        ip=ip,
        ts = f'{int(time())}'
    )
    print(f"{ip}")
    return HttpResponse(f"{ip}")

def get_ip(request):
    d = Ip.objects.all()[0]
    current_ts = int(time())
    last_ts = int(d.ts)
    ts_diff = current_ts - last_ts
    ip_exp = ts_diff > ip_exp_sec
    args = {'ip': d.ip, 'ts': d.ts, 'ip_exp': ip_exp}
    return JsonResponse(args)

def ip(request):
    d = Ip.objects.all()[0]
    args = {'ip': d.ip, 'ts': d.ts}
    return render(request, 'pages/ip.html', args)

def historical_data(request):
    d = request.GET["d"]
    start_raw = request.GET['sd']
    end_raw = request.GET['ed']

    sensor_data = []
    if ((start_raw == '-') and (end_raw == '-')):
        data = HistoricalData.objects.all()
    else:
        start_ts = int(mktime(datetime.datetime.strptime(start_raw, "%d-%m-%Y").timetuple()))
        end_ts = int(mktime(datetime.datetime.strptime(end_raw, "%d-%m-%Y").timetuple()))
        data = HistoricalData.objects.filter(ts__gte=start_ts, ts__lte=end_ts)
        print(start_ts, end_ts)


    if d == 'btemp':
        for i in data:
            if (i.body_temp != 0.0):
                sensor_data.append([i.ts*1000, i.body_temp, i.heart_rate])
    
    if d == 'hr':
        for i in data:
            if (i.heart_rate != 0.0):
                sensor_data.append([i.ts*1000, i.body_temp, i.heart_rate])

    if (len(sensor_data) > 50) and (start_raw == '-'):
        sensor_data = sensor_data[-50:]

    args = {'sensor_data': json.dumps(sensor_data), 'd': d}
    return render(request, 'pages/historical_data.html', args)

def tst(request):
    data = reversed(HistoricalData.objects.all())
    args = {'data': data}
    return render(request, 'pages/tst.html', args)
