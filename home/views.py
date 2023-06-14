import django
from urllib.parse import urlparse
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.exceptions import Resolver404
from django.urls.base import resolve, reverse
from django.views.generic import DetailView
from django.shortcuts import get_list_or_404
from django.utils import translation
from urllib.parse import urlparse

from .models import Bannercha, Book, Category, Images, MalImages, Malumotlar, Content, Fakultetlar, OqishniKochirish, Rektorat
from news.models import NewsCartegory, Yangiliklar


def page_not_found(request, exception):
    return render(request, 'custom_404.html', status=404)

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def index(request):


    context = {
        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8]
    }
    
    return render(request, "home/index.html", context)




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
        # "kontentla": kontentla
    }
    
    return render(request, "home/malumot.html", context)


def malumot_detail(request, cat_id):

    malumotlar = get_object_or_404(Malumotlar, id=cat_id)

    kontentcha = get_object_or_404(Malumotlar, id=cat_id)
    photos = MalImages.objects.filter(mal=kontentcha)

    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "cat_news": NewsCartegory.objects.filter(parent=None),
        "malumotlar": malumotlar,
        # "cat": Category.objects.get(name="UNIVERSITET"    ),
        "photos": photos,
    }

    return render(request, 'home/mailumot_detail.html', context)


def category(request, cat_id=None):
    catID = request.GET.get("cat")

    if catID:
        kontentla = Content.objects.filter(category__id=catID)
    
    else:
        kontentla = Content.objects.all()

    # kontentcha = get_object_or_404(Content, category__id=catID)
    # photos = Images.objects.filter(product=kontentcha)


    context = {
        "get_content": Content.objects.filter(category__id=cat_id) if cat_id else Content.objects.all(),
        'categories': Category.objects.filter(parent=None)[:6],
        "category": Category.objects.filter(id=cat_id),
        "cat": Category.objects.get(pk=cat_id),
        "cat_parent": get_object_or_404(Category, pk=catID),
        "fakultet": Category.objects.filter(parent_id=25),
        "kontentla": kontentla,
        # "photos": photos,
        # "kontentcha": kontentcha,
    }
    
    return render(request, "home/malumot.html", context)



# class MalumotDetailView(DetailView):
#     model = Malumotlar
#     template_name = 'home/mailumot_detail.html'
#     context_object_name = 'malumotlar'


def set_language(request, language):

    cat_ids = request.META.get('HTTP_REFERER')[-1::39]


    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            # view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
            print(view)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        if cat_ids:
            next_url += f"?cat={cat_ids}"
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
    





# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     pdf_url = book.pdf.url
#     return render(request, 'book_detail.html', {'book': book, 'pdf_url': pdf_url})


def download_pdf(request, book_id):
    book = get_object_or_404(Content, id=book_id)
    with open(book.pdf.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(book.pdf.name)
        return response


def rektorjon(request):
    
    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "category": Category.objects.filter(id=1),
        'rektorla': Rektorat.objects.all()
    }

    return render(request, "home/rektor.html", context)


def fakultet(request):
    
    context = {
        "fak": Fakultetlar.objects.all(),
        "category": Category.objects.filter(id=1),
        "CAT": Category.objects.filter(name="UNIVERSITET"),
        'categories': Category.objects.filter(parent=None)[:6],
    }

    return render(request, "home/fakultetlar.html", context)


def magistr(request):
    
    context = {
        "fak": Fakultetlar.objects.all(),
        "category": Category.objects.filter(id=1),
        "CAT": Category.objects.filter(name="UNIVERSITET"),
        'categories': Category.objects.filter(parent=None)[:6],
    }

    return render(request, "home/magistr.html", context)


def mailumot(request):
    
    context = {
        "fak": Fakultetlar.objects.all(),
        "category": Category.objects.filter(id=1),
        "CAT": Category.objects.filter(name="UNIVERSITET"),
        'categories': Category.objects.filter(parent=None)[:6],
    }

    return render(request, "home/malumot.html", context)


def sirtqi(request):
    
    context = {
        "fak": Fakultetlar.objects.all(),
        "category": Category.objects.filter(id=1),
        "CAT": Category.objects.filter(name="UNIVERSITET"),
        'categories': Category.objects.filter(parent=None)[:6],
    }

    return render(request, "home/sirtiq.html", context)


def oqishkochir(request):
    context = {
        "fak": Fakultetlar.objects.all(),
        "category": Category.objects.filter(id=1),
        "CAT": Category.objects.filter(name="UNIVERSITET"),
        'categories': Category.objects.filter(parent=None)[:6],
        'oqish': OqishniKochirish.objects.all(),
    }

    return render(request, "home/oqsh.html", context)

    