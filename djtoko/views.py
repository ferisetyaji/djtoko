from django.shortcuts import render, redirect

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
