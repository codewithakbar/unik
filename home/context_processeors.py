from .models import Category, Bannercha


def product_category_render(request):
    
    return {
        "banner": Bannercha.objects.all().order_by("-id")[:5],
        # 'categories': Category.objects.filter(parent=None)[:6],
    }
    