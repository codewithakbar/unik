from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="homepage"),
    path("malumotlar/", views.malumotlar, name="malumotlar"),
    path("malumotlar/<int:cat_id>", views.malumotlar, name="malumotlar"),
    path("malumot/<int:pk>/", views.MalumotDetailView.as_view(), name="malumot"),
    path("category/<int:cat_id>/", views.category, name="category"),
    path(r'set-language/', views.set_language, name='set_language'),

]
