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
	stok = models.CharField(max_length=100)
	nama_pemesan = models.CharField(max_length=100)
	alamat = models.CharField(max_length=500)
	status_pesanan = models.CharField(max_length=50)
	status_bayar = models.CharField(max_length=50)
	jumlah_bayar = models.IntegerField()
	total_bayar= models.IntegerField()