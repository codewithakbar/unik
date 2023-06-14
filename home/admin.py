from django.contrib import admin
from .models import (
    Bannercha,
    Category, Kunduz, Magistr, MalImages, Malumotlar, Content, 
                     Fakultetlar, Images, OqishniKochirish, Rektorat, Sirtqi, Book)

from modeltranslation.admin import TranslationAdmin

from mptt.admin import DraggableMPTTAdmin


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass


class ContentImagesInline(admin.StackedInline):
    model = Images


class MalumotlarImagesInline(admin.StackedInline):
    model = MalImages


class MalumotlarAdmin(TranslationAdmin):
    inlines = [MalumotlarImagesInline]
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


class ContentAdmin(TranslationAdmin):
    inlines = [ContentImagesInline]
    group_fieldsets = True
    fields = ('title', 'desc', 'category', ('nomi', 'summa'), ("rektor_image", "lavozim", "desc_rek"))

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class CategoryAdmin(DraggableMPTTAdmin, TranslationAdmin):
    group_fieldsets = True

    prepopulated_fields = {'slug': ('name',)}
    # list_display = ("name", )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    fields = ('name', 'slug', 'parent')
    # inlines = [CategoryLangInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Content,
                'category',
                'products_cumulative_count',
                cumulative=True)


        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Content,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs


    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'


    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'



class BannerAdmin(DraggableMPTTAdmin):
    fields = ('title', 'image', 'parent')
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')



admin.site.register(Bannercha, BannerAdmin)
admin.site.register(Malumotlar, MalumotlarAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Fakultetlar)
# admin.site.register(Kunduz)
# admin.site.register(Sirtqi)
# admin.site.register(OqishniKochirish)
# admin.site.register(Magistr)
# admin.site.register(Book)
# admin.site.register(Rektorat)
