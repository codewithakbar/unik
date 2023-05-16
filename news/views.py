from django.shortcuts import render

from .models import Yangiliklar, NewsCartegory


def news_view(request, cat_id=None):
    
    context = {
        "cat_news": NewsCartegory.objects.filter(parent=None),
        "catw": NewsCartegory.objects.get(pk=cat_id) if cat_id else NewsCartegory.objects.all(),
        "yangiliklar": Yangiliklar.objects.filter(category__id=cat_id) if cat_id else Yangiliklar.objects.all(),
    }

    return render(request, 'news/news.html', context)
