import datetime

from django.shortcuts import render, redirect

from ..models import Pesanan

def pesanan(request):

	if request.method == 'POST':
		del_pesanan = Pesanan.objects.get(id = request.POST['del'])
		del_pesanan.delete()
		return redirect('pesanan')

	data_pesanan = Pesanan.objects.all()
 
	return render(request, 'admin/pesanan.html', {'pesanan': data_pesanan})

def tambah_pesanan(request):

	if request.method == 'POST':

		q = Pesanan.objects.create(
				stok = request.POST['stok'],
				nama_pemesan = request.POST['nama_pemesan'],
				alamat = request.POST['alamat'],
				status_pesanan = 'Baru',
				status_bayar = request.POST['status_bayar'],
				jumlah_bayar = isset(request.POST['jumlah_bayar']),
				total_bayar = isset(request.POST['total_bayar'])
			)

		q.save
		return redirect('pesanan')

	data = {

		'title': 'Tambah ',

	}

	return render(request, 'admin/pesanan_form.html', data)

def edit_pesanan(request, pesanan_id):

	data_pesanan = Pesanan.objects.get(id = pesanan_id)

	if request.method == 'POST':

		Pesanan.objects.filter(id = pesanan_id).update(
				stok = request.POST['stok'],
				nama_pemesan = request.POST['nama_pemesan'],
				alamat = request.POST['alamat'],
				status_pesanan = 'Baru',
				status_bayar = request.POST['status_bayar'],
				jumlah_bayar = isset(request.POST['jumlah_bayar']),
				total_bayar = isset(request.POST['total_bayar'])
			)

		return redirect('pesanan')

	data = {
		'title' : 'Edit ',
		'pesanan_id' : data_pesanan,
	}

	return render(request, 'admin/pesanan_form.html', data)


def isset(field):
	if not field:
		return 0;
	else:
		return field

def convert(string): 
    li = list(string.split(" ")) 
    return li
