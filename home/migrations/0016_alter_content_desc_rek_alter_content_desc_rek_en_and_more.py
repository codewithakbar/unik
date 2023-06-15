# Generated by Django 4.2.1 on 2023-06-15 18:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_content_desc_rek_en_content_desc_rek_ru_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="desc_rek",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Rektorlar Descriptioni"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="desc_rek_en",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Rektorlar Descriptioni"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="desc_rek_ru",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Rektorlar Descriptioni"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="desc_rek_uz",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Rektorlar Descriptioni"
            ),
        ),
    ]
