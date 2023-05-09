from django.contrib import admin

from .models import Yangiliklar


@admin.register(Yangiliklar)
class NewsAdmin(admin.ModelAdmin):
    pass

