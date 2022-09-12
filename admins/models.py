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
	telp = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	alamat = models.CharField(max_length=500)
	status_pesanan = models.CharField(max_length=50)
	jumlah = models.IntegerField()
	harga = models.IntegerField()
	subtotal= models.IntegerField()

class Customer(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	nama_lengkap = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	telp = models.CharField(max_length=200)
	alamat = models.TextField()
	