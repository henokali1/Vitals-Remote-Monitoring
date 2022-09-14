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


class HomePageView(TemplateView):
    template_name = 'home.html'

def live(request):
	args={}
	return render(request, 'pages/live.html', args)
