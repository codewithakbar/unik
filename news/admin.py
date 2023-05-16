from django.contrib import admin

from .models import Yangiliklar, NewsCartegory



@admin.register(NewsCartegory)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Yangiliklar)
class NewsAdmin(admin.ModelAdmin):
    pass

