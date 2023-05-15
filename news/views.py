from django.shortcuts import render

from .models import Yangiliklar


def news_view(request):

    context = {
        "rte": "dkfa"
    }

    return render(request, 'news/news.html', context)