from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Banner


def index(request):
    
    context = {
        "banner": Banner.objects.all().order_by("-id")[:5],
    }
    return render(request, "home/index.html", context)


# @login_required
def set_language(request):
    lang = request.GET.get('l', 'en')
    request.session[settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response