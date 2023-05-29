from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.news_view, name="news"),
    path("news/<int:cat_id>/", views.news_view, name="news_cat"),
    path("detail/<int:cat_id>/", views.new_detail, name="new_detail"),
    # path(r'set-language/', views.set_language, name='set_language'),

]
