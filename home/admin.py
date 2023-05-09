from django.contrib import admin

from .models import Banner, Category

# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Banner)
admin.site.register(Category)

