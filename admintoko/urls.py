from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views.users import UserView, addUserView, editUserView
from .views import stok
from .views import kategori

urlpatterns = [
    path('', TemplateView.as_view(template_name='admin/dashboard.html'), name='dashboard'),
    path('user/', UserView.as_view(template_name='admin/user.html'), name='user'),
    path('user/tambah_user', addUserView.as_view(template_name='admin/user_form.html'), name='tambah_user'),
    path('user/edit_user/<id>', editUserView.as_view(template_name='admin/user_form.html'), name='edit_user'),
    path('stok/', stok.stok, name='stok'),
	path('tambah_stok', stok.tambah_stok, name='tambah_stok'),
	path('edit_stok/<int:stok_id>/', stok.edit_stok, name='edit_stok'),
	path('kategori/', kategori.kategori, name='kategori'),
	path('tambah_kategori', kategori.tambah_kategori, name='tambah_kategori'),
	path('edit_kategori/<int:kategori_id>/', kategori.edit_kategori, name='edit_kategori'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)