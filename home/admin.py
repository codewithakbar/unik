from django.contrib import admin

from .models import Banner, Category, Malumotlar, Content, Fakultetlar

# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # pass

admin.site.register(Banner)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Malumotlar)
admin.site.register(Content)
admin.site.register(Fakultetlar)
