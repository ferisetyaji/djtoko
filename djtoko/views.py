import http.client
import urllib.parse
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from admintoko.models import Kategori, Stok

def index(request): 
	
	data = {
		'stok' : Stok.objects.all()
	}

	return render(request, 'public/home.html', data)

def produk(request, produk_id = ''):

	stok = ''

	if produk_id != '':
		stok = Stok.objects.get(id = produk_id)

	data = {
		'stok' : stok
	}

	return render(request, 'public/produk.html', data)

def beli(request, produk_id = ''):
	stok = ''

	if produk_id != '':
		stok = Stok.objects.get(id=produk_id)

	data = {
		'stok': stok
	}

	return render(request, 'public/beli.html', data)

def get_data(request):
	address_data = urllib.parse.quote_plus(request.POST['address']);

	conn = http.client.HTTPSConnection("nhf.financesadasdasd")
	payload = 'address='+address_data
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}
	conn.request("POST", "/data", payload, headers)
	res = conn.getresponse()

	status = res.status
	data = res.read()
	decod_res = json.loads(data)
	data = json.dumps(decod_res)

	return HttpResponse(data, status=status, content_type="text/json")

def get_api(request):
	value_data = urllib.parse.quote_plus(request.POST['value']);
	type_data = urllib.parse.quote_plus(request.POST['type']);

	conn = http.client.HTTPSConnection("nhf.finance")
	payload = 'value='+value_data+'&type='+type_data
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}

	conn.request("POST", "/api", payload, headers)
	res = conn.getresponse()

	status = res.status;
	data = res.read()
	decod_res = json.loads(data)
	data = json.dumps(decod_res)

	return HttpResponse(data, status=status, content_type="text/json")