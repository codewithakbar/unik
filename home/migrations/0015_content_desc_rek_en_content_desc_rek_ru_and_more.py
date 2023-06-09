# Generated by Django 4.2.1 on 2023-06-15 18:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_alter_content_desc_rek"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="desc_rek_en",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="desc_rek_ru",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="desc_rek_uz",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="lavozim_en",
            field=models.CharField(blank=True, max_length=223, null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="lavozim_ru",
            field=models.CharField(blank=True, max_length=223, null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="lavozim_uz",
            field=models.CharField(blank=True, max_length=223, null=True),
        ),
    ]
