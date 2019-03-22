from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
import time
# Create your views here.

def tmp(request):
	data2 = {}
	data2['name'] = 'yjw'
	lists = ['嘤嘤嘤','切克闹']
	name = '大爷来玩儿'
	data1 = ['首页','女装','汉服','cosplay']
	return render(request,'home/tmp.html',{'info':data2,'list':lists,'name':name,'data1':data1})
