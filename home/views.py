from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.shortcuts import get_list_or_404

from .models import Banner, Category, Malumotlar, Content
from news.models import NewsCartegory, Yangiliklar


def index(request):


    context = {
        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
    }
    
    return render(request, "home/index.html", context)


def fakultet(request):
    
    context = {
        "kontentla": "kontentla",
        'categories': Category.objects.filter(parent=None)[:6],
        "category": Category.objects.filter(parent_id=1),
    }

    return render(request, "home/fakultetlar.html", context)


def malumotlar(request):

    catID = request.GET.get("cat")

    if catID:
        kontentla = Content.objects.filter(category__id=catID)
    
    else:
        kontentla = Content.objects.all()

    # products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "malumotlar": Malumotlar.objects.all(),
        "kontentla": kontentla
    }
    
    return render(request, "home/malumot.html", context)


def malumot_detail(request, cat_id):

    malumotlar = get_object_or_404(Malumotlar, id=cat_id)

    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "cat_news": NewsCartegory.objects.filter(parent=None),
        "malumotlar": malumotlar,
    }

    return render(request, 'home/mailumot_detail.html', context)




def category(request, cat_id=None):
    catID = request.GET.get("cat")

    if catID:
        kontentla = Content.objects.filter(category__id=catID)
    
    else:
        kontentla = Content.objects.all()
    context = {
        "get_content": Content.objects.filter(category__id=cat_id) if cat_id else Content.objects.all(),
        'categories': Category.objects.filter(parent=None)[:6],
        "category": Category.objects.filter(id=cat_id),
        "cat": Category.objects.get(pk=cat_id),
        "cat_parent": Category.objects.get(pk=cat_id),
        "kontentla": kontentla,
    }
    
    return render(request, "home/malumot.html", context)


def rektorjon(request):
    
    context = {
        "kontentla": "kontentla",
        'categories': Category.objects.filter(parent=None)[:6],
        "category": Category.objects.filter(parent_id=1),
    }

    return render(request, "home/rektor.html", context)


class MalumotDetailView(DetailView):
    model = Malumotlar
    template_name = 'home/mailumot_detail.html'
    context_object_name = 'malumotlar'


# @login_required
def set_language(request):
    lang = request.GET.get('l', 'en')
    request.session[settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


