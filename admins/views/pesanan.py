import datetime

from django.shortcuts import render, redirect

from ..models import Pesanan

def pesanan(request):

	if request.method == 'POST':

		if 'batal' in request.POST:
			del_pesanan = Pesanan.objects.get(id = request.POST['batal'])
			del_pesanan.delete()

		if 'kirim' in request.POST:
			Pesanan.objects.filter(id = request.POST['kirim']).update(status_pesanan = 'pesanan_dikirim')

		if 'terkirim' in request.POST:
			Pesanan.objects.filter(id = request.POST['terkirim']).update(status_pesanan = 'pesanan_terkirim')

		return redirect('pesanan')

	data_pesanan = Pesanan.objects.all()
 
	return render(request, 'admin/pesanan.html', {'pesanan': data_pesanan})

def tambah_pesanan(request):

	if request.method == 'POST':

		q = Pesanan.objects.create(
				id_stok = request.POST['stok'],
				nama_pemesan = request.POST['nama_pemesan'],
				alamat = request.POST['alamat'],
				status_pesanan = 'Baru',
				jumlah = isset(request.POST['jumlah']),
				harga = isset(request.POST['harga']),
				subtotal = isset(request.POST['subtotal'])
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
				jumlah = isset(request.POST['jumlah']),
				harga = isset(request.POST['harga']),
				subtotal = isset(request.POST['subtotal'])
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
