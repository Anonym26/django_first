# Generated by Django 4.0.5 on 2022-06-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, height_field=350, null=True, upload_to='photos/%Y/Ym/%d', verbose_name='Ссылка на изображение', width_field=150),
        ),
    ]