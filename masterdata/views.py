# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from masterdata.models import SD_Creation, MD_Creation
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.apps import apps



# Create your views here.
def list_sd_creation(request):
	if request.method == 'GET':
		obj = apps.get_model('masterdata','SD_Creation')
		obj_json = list(obj.objects.values())
		obj_data = {'status':True,"data":obj_json}
		return JsonResponse(obj_data)
	elif request.method == 'POST':
		return HttpResponse('POST')

@csrf_exempt
def add_sd_creation(request):
	if request.method == 'POST':
		#import ipdb;ipdb.set_trace()
		name = request.POST.get("name")
		creation_name = request.POST.get("creation_name")
		SD_Creation.objects.create(name=name,creation_name=creation_name)
		obj_data = {"message":"Successfully added","status":True}
		return JsonResponse(obj_data)
@csrf_exempt
def edit_sd_creation(request,pk):
	if request.method == 'GET':
		obj = SD_Creation.objects.get(pk=pk)
		json_data = {"name":obj.name,"creation_name":obj.creation_name}
		obj_data = {"data":json_data,"status":True}
		return JsonResponse(obj_data)

	if request.method == 'POST':
		name = request.POST.get("name")
		creation_name = request.POST.get("creation_name")
		obj = SD_Creation.objects.get(pk=pk)

		obj.name = name
		obj.creation_name = creation_name
		obj.save()
		obj_data = {"message":"Successfully Updated","status":True}
		return JsonResponse(obj_data)

def delete_sd_creation(request,pk):
	obj = SD_Creation.objects.get(pk=pk)
	obj.delete()
	obj_data = {"message":"Successfully Deleted","status":True}
	return JsonResponse(obj_data)