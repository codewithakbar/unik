from django.contrib import admin

from .models import Yangiliklar, NewsCartegory

from modeltranslation.admin import TranslationAdmin


@admin.register(NewsCartegory)
class NewsAdmin(TranslationAdmin, admin.ModelAdmin):

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Yangiliklar)
class NewsAdmin(TranslationAdmin):

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


    pass

