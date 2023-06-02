from django.contrib import admin
from .models import (
    Banner, Category, Kunduz, Magistr, MalImages, Malumotlar, Content, 
                     Fakultetlar, Images, OqishniKochirish, Rektorat, Sirtqi, Book)

from modeltranslation.admin import TranslationAdmin


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


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    group_fieldsets = True

    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(Banner)

admin.site.register(Malumotlar, MalumotlarAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Fakultetlar)
admin.site.register(Kunduz)
admin.site.register(Sirtqi)
admin.site.register(OqishniKochirish)
admin.site.register(Magistr)
admin.site.register(Book)
admin.site.register(Rektorat)
