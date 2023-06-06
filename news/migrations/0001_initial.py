# Generated by Django 4.2.1 on 2023-06-03 12:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsCartegory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=211)),
                ("slug", models.SlugField(unique=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="news.newscartegory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Yangiliklar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=232)),
                ("desc", ckeditor.fields.RichTextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="news/%Y/%m/%d", null=True, upload_to=""
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.newscartegory",
                    ),
                ),
            ],
        ),
    ]
