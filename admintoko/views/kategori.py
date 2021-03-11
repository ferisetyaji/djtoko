from django.shortcuts import render, redirect

from ..models import Kategori

def kategori(request):

	if request.method == 'POST':
		del_kategori = Kategori.objects.get(id = request.POST['del'])
		del_kategori.delete()
		return redirect('kategori')

	data_kategori = Kategori.objects.all()
 
	return render(request, 'admin/kategori.html', {'kategori': data_kategori})

def tambah_kategori(request):

	if request.method == 'POST':

		slug = request.POST['nama']
		slug = slug.split()
		slug = '-'.join(slug)

		q = Kategori.objects.create(
				nama = request.POST['nama'],
				slug = slug
			)

		q.save
		return redirect('kategori')

	return render(request, 'admin/kategori_form.html', {'title': 'Tambah '})

def edit_kategori(request, kategori_id):

	data_kategori = Kategori.objects.get(id = kategori_id)

	if request.method == 'POST':

		slug = request.POST['nama']
		slug = slug.split()
		slug = '-'.join(slug)

		Kategori.objects.filter(id = kategori_id).update(
				nama = request.POST['nama'],
				slug = slug
			)

		return redirect('kategori')

	data = {
		'title' : 'Edit ',
		'kategori_id' : data_kategori
	}

	return render(request, 'admin/kategori_form.html', data)


def isset(field):
	if not field:
		return 0;
	else:
		return field

	