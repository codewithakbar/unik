from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from home.models import Category

from .models import Yangiliklar, NewsCartegory



def news_view(request, cat_id=None):
    
    context = {
        "cat_news": NewsCartegory.objects.filter(parent=None),
        'categories': Category.objects.filter(parent=None)[:6],
        "catw": NewsCartegory.objects.get(pk=cat_id) if cat_id else NewsCartegory.objects.all(),
        "yangiliklar": Yangiliklar.objects.filter(category__id=cat_id) if cat_id else Yangiliklar.objects.all(),
    }

    return render(request, 'news/news.html', context)


def new_detail(request, cat_id):

    yangilik = get_object_or_404(Yangiliklar, id=cat_id)

    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "cat_news": NewsCartegory.objects.filter(parent=None),
        "yangilik": yangilik
    }

    return render(request, 'news/news_detail.html', context)

