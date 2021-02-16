import datetime
import tempfile
import shutil

FILE_UPLOAD_DIR = 'static/img'

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

		myfile = request.FILES['file']
		
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)

		q = Stok.objects.create(
				nama = request.POST['nama'],
				deskripsi = request.POST['deskripsi'],
				harga = isset(request.POST['harga']),
				kategori = request.POST['kategori'],
				gambar = filename,
				tanggal = datetime.datetime.now()
			)

		q.save
		return redirect('stok')

	return render(request, 'admin/stok_form.html', {'title': 'Tambah '})

def edit_stok(request, stok_id):

	data_stok = Stok.objects.get(id = stok_id)

	if request.method == 'POST':

		q = Stok.objects.filter(id = stok_id).update(
				nama = request.POST['nama'],
				deskripsi = request.POST['deskripsi'],
				harga = isset(request.POST['harga']),
				kategori = request.POST['kategori'],
				jumlah_stok = request.POST['stok'],
			)

		return redirect('stok')

	data = {
		'title' : 'Edit ',
		'user' : data_stok
	}

	return render(request, ' admin/stok_form.html', data)

def handle_uploaded_file(source):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    return filepath


def isset(field):
	if not field:
		return 0;
	else:
		return field

	