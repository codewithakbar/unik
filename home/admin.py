from django.contrib import admin

from .models import (
    Banner, Category, Kunduz, Magistr, MalImages, Malumotlar, Content, 
                     Fakultetlar, Images, OqishniKochirish, Sirtqi, Book)


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass

class ContentImagesInline(admin.StackedInline):
    model = Images

class MalumotlarImagesInline(admin.StackedInline):
    model = MalImages


class MalumotlarAdmin(admin.ModelAdmin):
    inlines = [MalumotlarImagesInline]


class ContentAdmin(admin.ModelAdmin):
    inlines = [ContentImagesInline]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # pass


admin.site.register(Banner)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Malumotlar, MalumotlarAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Fakultetlar)
admin.site.register(Kunduz)
admin.site.register(Sirtqi)
admin.site.register(OqishniKochirish)
admin.site.register(Magistr)
admin.site.register(Book)
