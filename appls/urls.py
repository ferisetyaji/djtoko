from django.urls import path

from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('user/', views.user, name='user'),
	path('tambah_user', views.tambah_user, name='tambah_user'),
	path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
]