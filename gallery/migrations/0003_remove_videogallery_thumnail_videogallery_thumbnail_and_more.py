# Generated by Django 4.2.1 on 2023-07-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_videogallery_thumnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogallery',
            name='thumnail',
        ),
        migrations.AddField(
            model_name='videogallery',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='thumbnail/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videogallery',
            name='video',
            field=models.FileField(upload_to='gallery/video/%Y/%m/%d'),
        ),
    ]
