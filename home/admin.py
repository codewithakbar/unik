from django.contrib import admin

from .models import Banner, Category, Malumotlar

# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # pass

admin.site.register(Banner)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Malumotlar)

