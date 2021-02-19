import datetime

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ..models import Stok

def stok(request):

	if request.method == 'POST':
		del_stok = Stok.objects.get(id = request.POST['del'])
		del_stok.delete()
		return redirect('stok')

	data_stok = Stok.objects.all()
 
	return render(request, 'admin/stok.html', {'stok': data_stok})

def tambah_stok(request):

	if request.method == 'POST':

		filename = ''

		if 'file' in request.FILES:
			myfile = request.FILES['file']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		q = Stok.objects.create(
				nama = request.POST['nama'],
				deskripsi = request.POST['deskripsi'],
				harga = isset(request.POST['harga']),
				kategori = request.POST['kategori'],
				gambar = filename,
				tanggal = datetime.datetime.now(),
				jumlah_stok = isset(request.POST['jumlah'])
			)

		q.save
		return redirect('stok')

	return render(request, 'admin/stok_form.html', {'title': 'Tambah '})

def edit_stok(request, stok_id):

	data_stok = Stok.objects.get(id = stok_id)

	if request.method == 'POST':

		if 'file' in request.FILES:
			myfile = request.FILES['file']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			Stok.objects.filter(id = stok_id).update(gambar = filename)

		Stok.objects.filter(id = stok_id).update(
				nama = request.POST['nama'],
				deskripsi = request.POST['deskripsi'],
				harga = isset(request.POST['harga']),
				kategori = request.POST['kategori'],
				jumlah_stok = isset(request.POST['jumlah'])
			)

		return redirect('stok')

	data = {
		'title' : 'Edit ',
		'stok_id' : data_stok
	}

	return render(request, 'admin/stok_form.html', data)


def isset(field):
	if not field:
		return 0;
	else:
		return field

	