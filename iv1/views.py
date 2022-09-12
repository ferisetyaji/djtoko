from django.shortcuts import render, redirect

from admins.models import Stok, Customer

def index(request):

	if 'id' not in request.session:
		return redirect('login')

	data = {
		'stok' : Stok.objects.all()
	}

	return  render(request, 'public/home.html', data)

def produk(request, produk_id = ''):

	stok = ''

	if produk_id != '':
		stok = Stok.objects.get(id = produk_id)

	data = {
		'stok' : stok
	}

	return render(request, 'public/produk.html', data)

def checkout(request):
	return render(request, 'public/checkout.html')
    
def register(request):

	if request.method == 'POST':
		q = Customer.objects.create(
				username = request.POST['username'],
				password = request.POST['password'],
				nama_lengkap = request.POST['nama_lengkap'],
				email = request.POST['email'],
				telp = request.POST['telp'],
				alamat = request.POST['alamat']
			)

		q.save
		return redirect('home')

	return render(request, 'public/register.html')

def login(request):

	if request.method == 'POST':
		user = Customer.objects.filter(username=request.POST['username'], password=request.POST['password']).values()
		request.session['id'] = user[0]['id']

		return redirect('home')
	
	return render(request, 'public/login.html')

def logout(request):
	del request.session['id']
	return redirect('login')