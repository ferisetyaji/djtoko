from django.shortcuts import render, redirect
from .models import Users

def dashboard(request):
	return render(request, 'admin/dashboard.html')

def user(request):

	if request.method == 'POST':
		del_user = Users.objects.get(id = request.POST['del'])
		del_user.delete()
		return redirect('user')

	data_user = Users.objects.all()

	return render(request, 'admin/user.html', {'user': data_user})

def tambah_user(request):

	if request.method == 'POST':

		q = Users.objects.create(
				username = request.POST['name'],
				password = request.POST['pass']
			)

		q.save
		return redirect('user')

	return render(request, 'admin/user_form.html', {'title': 'Tambah '})

def edit_user(request, user_id):

	data_user = Users.objects.get(id = user_id)

	if request.method == 'POST':

		q = Users.objects.filter(id = user_id).update(
				username = request.POST['name'],
				password = request.POST['pass']
			)

		return redirect('user')

	data = {
		'title' : 'Edit ',
		'user' : data_user
	}

	return render(request, 'admin/user_form.html', data)