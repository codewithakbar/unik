# Generated by Django 4.2.1 on 2023-06-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_content_desc_alter_content_desc_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='desc_rek',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='lavozim',
            field=models.CharField(blank=True, max_length=223),
        ),
        migrations.AddField(
            model_name='content',
            name='rektor_image',
            field=models.ImageField(blank=True, null=True, upload_to='rektor/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=224),
        ),
        migrations.AlterField(
            model_name='content',
            name='title_en',
            field=models.CharField(max_length=224, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title_ru',
            field=models.CharField(max_length=224, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title_uz',
            field=models.CharField(max_length=224, null=True),
        ),
    ]
