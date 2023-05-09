from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.index, name="yangiliklar"),
    path(r'set-language/', views.set_language, name='set_language'),

]
