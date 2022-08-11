from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from ..models import Users

class ApiView(TemplateView):

	def get_context_data(self, **kwargs):

		id_user = super().get_context_data(**kwargs)

		user_id = []

		if 'id' in id_user.keys():
			user_id = Users.objects.get(id = id_user['id'])
			

		data_user = Users.objects.all()

		context = {

			'user' : data_user,
			'user_id' : user_id

		}

		return context

	def post(self, request, *args, **kwargs):

		if request.method == 'POST':
			
			del_user = Users.objects.get(id = request.POST['del'])
			del_user.delete()
			return redirect('user')


class addUserView(TemplateView):
	
	def post(self, request, *args, **kwargs):

		q = Users.objects.create(
				username = request.POST['name'],
				password = request.POST['pass']
			)

		q.save
		return redirect('user')


class editUserView(TemplateView):

	def get_context_data(self, **kwargs):

		id_user = super().get_context_data(**kwargs)

		if 'id' in id_user.keys():
			user_id = Users.objects.get(id = id_user['id'])
			

		data_user = Users.objects.all()

		context = {

			'user_id' : user_id

		}

		return context
	
	def post(self, request, *args, **kwargs):

		q = Users.objects.filter(id = request.POST['id']).update(
				username = request.POST['name'],
				password = request.POST['pass']
			)

		return redirect('user')