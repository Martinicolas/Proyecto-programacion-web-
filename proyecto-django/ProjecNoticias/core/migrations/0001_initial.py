# Generated by Django 4.2.1 on 2023-06-20 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('codigo', models.CharField(max_length=5,
                 primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Rango', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True,
                 upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
    ]
