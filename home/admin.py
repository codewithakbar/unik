from django.contrib import admin

from .models import Banner, Category, Malumotlar, Content, Fakultetlar


# 404
class FakultetlarInline(admin.TabularInline):
   model = Fakultetlar
   extra = 1

# karoche inline qilib bo'lmadi sababi 
# Forinkey ulanishi keriak akan
# @admin.register(Fakultetlar)
# class FakultetlarAdmin(admin.ModelAdmin):
#     inlines = (FakultetlarInline,)


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

