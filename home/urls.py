from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="homepage"),
    path("malumotlar/", views.malumotlar, name="malumotlar"),
    path("malumotlar/<int:cat_id>/", views.malumotlar, name="malumot"),
    path("malumot/<int:cat_id>/", views.malumot_detail, name="malumot_detail"),
    path("category/rektorat/", views.rektorjon, name="rektorlar"),
    path("category/<int:cat_id>/", views.category, name="category"),
    path(r'set-language/', views.set_language, name='set_language'),

]
