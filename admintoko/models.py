from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Stok(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField()
	harga = models.IntegerField()
	kategori = models.CharField(max_length=20)
	gambar = models.CharField(max_length=50)
	tanggal = models.DateTimeField()

class Kategori(models.Model):
	nama = models.CharField(max_length=100)