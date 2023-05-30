import django
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="homepage"),
    path("malumotlar/", views.malumotlar, name="malumotlar"),
    path("malumotlar/<int:cat_id>/", views.malumotlar, name="malumot"),
    path("malumot/<int:cat_id>/", views.malumot_detail, name="malumot_detail"),
    path("category/<int:cat_id>/", views.category, name="category"),
    path(r'set-language/', views.set_language, name='set_language'),

    # 404

    path("404/", views.custom_page_not_found),



    # no category for page
    path("category/rektorat/", views.rektorjon, name="rektorlar"),
    path("fakultet/", views.fakultet, name="fakultet"),
    path("magistr/", views.magistr, name="magistr"),
    path("mailumot/", views.mailumot, name="mailumot"),
    path("sirtqi/", views.sirtqi, name="sirtqi"),
    path("oqishkochir/", views.oqishkochir, name="oqishkochir"),

    #book pdf

    path('books/<int:book_id>/download/', views.download_pdf, name='download_pdf'),
]

handler404 = "home.views.page_not_found"


