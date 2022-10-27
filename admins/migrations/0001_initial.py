# Generated by Django 4.1.1 on 2022-10-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('foto', models.TextField()),
                ('telp', models.CharField(max_length=200)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_stok', models.IntegerField()),
                ('id_pemesan', models.IntegerField()),
                ('nama_pemesan', models.CharField(max_length=100)),
                ('nama_produk', models.CharField(max_length=100)),
                ('telp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=500)),
                ('status_pesanan', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField()),
                ('harga', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('rating', models.IntegerField(blank=True, default=None, null=True)),
                ('komentar', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('harga', models.IntegerField()),
                ('kategori', models.CharField(max_length=20)),
                ('gambar', models.CharField(max_length=100)),
                ('tanggal', models.DateTimeField()),
                ('jumlah_stok', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
