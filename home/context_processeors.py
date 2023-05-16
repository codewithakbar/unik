from .models import Category


def product_category_render(request):
    
    return {
        'categories': Category.objects.filter(parent=None)[:6]
    }
    