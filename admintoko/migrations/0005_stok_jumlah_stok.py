# Generated by Django 3.1.4 on 2021-02-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintoko', '0004_stok_gambar'),
    ]

    operations = [
        migrations.AddField(
            model_name='stok',
            name='jumlah_stok',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
