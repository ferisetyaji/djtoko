from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from ..models import Users

class HomeView(TemplateView):
	pass

class UserView(TemplateView):

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
