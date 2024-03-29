from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Stok(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField()
	harga = models.IntegerField()
	kategori = models.CharField(max_length=20)
	gambar = models.CharField(max_length=100)
	tanggal = models.DateTimeField()
	jumlah_stok = models.IntegerField()

class Kategori(models.Model):
	nama = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)

class Pesanan(models.Model):
	id_stok = models.IntegerField()
	id_pemesan = models.IntegerField()
	nama_pemesan = models.CharField(max_length=100)
	nama_produk = models.CharField(max_length=100)
	telp = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	alamat = models.CharField(max_length=500)
	status_pesanan = models.CharField(max_length=50)
	jumlah = models.IntegerField()
	harga = models.IntegerField()
	subtotal= models.IntegerField()
	rating= models.IntegerField(null=True, default=None, blank=True)
	komentar= models.TextField(null=True, default=None, blank=True)

class Customer(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	nama_lengkap = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	foto = models.TextField()
	telp = models.CharField(max_length=200)
	alamat = models.TextField()

class Slide(models.Model):
	gambar = models.TextField()
	link = models.TextField()