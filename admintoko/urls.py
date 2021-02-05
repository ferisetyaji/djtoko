from django.urls import path, include

from .views.users import HomeView, UserView

urlpatterns = [
    path('', HomeView.as_view(template_name='admin/dashboard.html'), name='dashboard'),
    path('user/', UserView.as_view(template_name='admin/user.html'), name='user'),
    path('user/tambah_user', UserView.as_view(template_name='admin/user_form.html'), name='tambah_user'),
    path('user/edit_user/<id>', UserView.as_view(template_name='admin/user_form.html'), name='edit_user'),
]