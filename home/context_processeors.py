from .models import Category, Banner


def product_category_render(request):
    
    return {
        "banner": Banner.objects.all().order_by("-id")[:5],
        'categories': Category.objects.filter(parent=None)[:6],
    }
    