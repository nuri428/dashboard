from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path("news/news_tables", views.news_tables, name="news_tables"),    
]