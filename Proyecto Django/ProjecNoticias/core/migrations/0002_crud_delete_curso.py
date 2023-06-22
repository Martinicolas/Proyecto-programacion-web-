# Generated by Django 4.2.1 on 2023-06-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('codigo', models.CharField(max_length=5,
                 primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Rango', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True,
                 upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
        migrations.DeleteModel(
            name='curso',
        ),
    ]
