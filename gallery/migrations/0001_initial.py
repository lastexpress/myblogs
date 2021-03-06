# Generated by Django 3.2.7 on 2021-09-23 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=50, verbose_name='Заголовок категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('-cat_title',),
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gal_title', models.CharField(max_length=20, verbose_name='Название картинки')),
                ('gal_img', models.ImageField(upload_to='galleryimg/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
            ],
            options={
                'ordering': ('-gal_title',),
            },
        ),
    ]
