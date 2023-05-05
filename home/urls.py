from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="homepage"),
    path(r'set-language/', views.set_language, name='set_language'),

]
