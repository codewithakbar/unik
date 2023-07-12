from django.shortcuts import render

from home.models import Bannercha, Category, HomeSlider, Malumotlar
from news.models import Yangiliklar

from .models import TopBanner, GalleryImages, VideoGallery


def gallery(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/glavnaya.html", context)


def foto(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/foto.html", context)


def video(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/video.html", context)