import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from ..models import Users, Stok, Pesanan, Customer

def get(request):
	response_data = {}
	response_data['user'] = list(Users.objects.values())
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def tambah_keranjang(request):

	data = None

	if request.method == 'POST':
		id = 1
		form_data = json.loads(request.POST['keranjang'])
		form_data1 = set(form_data)
		form_data1 = list(form_data1);
		
		items = []
		for item in form_data1:
			
			j_item = 0;
			for i in form_data:
				if item == i:
					j_item+=1

			dt_item = Stok.objects.filter(id = item)[0]

			if(j_item < dt_item.jumlah_stok):
				items.append({
						'id' : item,      
						'nama' : dt_item.nama,
						'harga' : dt_item.harga,
						'kategori' : dt_item.kategori,
						'gambar' : dt_item.gambar,
						'jumlah' : j_item
					})

		data = json.dumps(items)

	return HttpResponse(data, content_type="text/json-comment-filtered")

def get_keranjang(request):
	data = None
	if request.method == 'POST':
		form_data = json.loads(request.POST['keranjang'])
		print(form_data)
		form_data1 = set(form_data)
		form_data = list(form_data1)
		
		items = []
		for i in form_data:
			dt_item = Stok.objects.filter(id = i)[0]
			items.append({
						'id' : dt_item.id,      
						'nama' : dt_item.nama,
						'deskripsi' : dt_item.deskripsi,
						'harga' : dt_item.harga,
						'kategori' : dt_item.kategori,
						'gambar' : dt_item.gambar,
						'tanggal' : dt_item.tanggal,
						'jumlah' : dt_item.jumlah_stok
					})

		data = json.dumps(items, indent=4, sort_keys=True, default=str)

	return HttpResponse(data, content_type="text/json-comment-filtered")

def bayar(request):
	data = None
	if request.method == 'POST':
		item = json.loads(request.POST['item'])
		items = []
		for i in item:
			dt_item = Stok.objects.filter(id = i['id'])[0]
			subtotal = int(dt_item.harga) * int(i['jml'])
			q = Pesanan.objects.create(
				id_stok = i['id'],
				id_pemesan = request.POST['id'],
				nama_pemesan = request.POST['full_name'],
				telp = request.POST['telp'],
				email = request.POST['email'],
				alamat = request.POST['alamat'],
				status_pesanan = 'pesanan_belum_diproses',
				jumlah = i['jml'],
				harga = dt_item.harga,
				subtotal = subtotal
				)
			q.save

			items.append({
						'id' : dt_item.id,      
						'nama' : dt_item.nama,
						'deskripsi' : dt_item.deskripsi,
						'harga' : dt_item.harga,
						'kategori' : dt_item.kategori,
						'gambar' : dt_item.gambar,
						'tanggal' : dt_item.tanggal,
						'jumlah' : dt_item.jumlah_stok,
						'status' : 'pesanan_belum_diproses'
					})

		item_detail = json.dumps(items, indent=4, sort_keys=True, default=str)
		data = '{"item":'+item_detail+',"message":"success"}';
	return HttpResponse(data, content_type="text/json-comment-filtered")

def customer(request):
	cs = Customer.objects.filter(id = request.session['id']).values()[0]
	data = json.dumps(cs, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")
