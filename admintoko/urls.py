from django.urls import path, include
from django.views.generic.base import TemplateView

from .views.users import UserView, addUserView, editUserView

urlpatterns = [
    path('', TemplateView.as_view(template_name='admin/dashboard.html'), name='dashboard'),
    path('user/', UserView.as_view(template_name='admin/user.html'), name='user'),
    path('user/tambah_user', addUserView.as_view(template_name='admin/user_form.html'), name='tambah_user'),
    path('user/edit_user/<id>', editUserView.as_view(template_name='admin/user_form.html'), name='edit_user'),
]