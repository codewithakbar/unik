from django.contrib import admin

from .models import Banner, Category, Kunduz, Magistr, Malumotlar, Content, Fakultetlar, Images, OqishniKochirish, Sirtqi

# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # pass


class ContentImagesInline(admin.StackedInline):
    model = Images


class ContentAdmin(admin.ModelAdmin):
    inlines = [ContentImagesInline]


admin.site.register(Banner)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Malumotlar)
admin.site.register(Content, ContentAdmin)
admin.site.register(Fakultetlar)
admin.site.register(Kunduz)
admin.site.register(Sirtqi)
admin.site.register(OqishniKochirish)
admin.site.register(Magistr)
