from django.urls import path

from . import views

urlpatterns = [    
    path("news/news_tables", views.news_tables, name="news_tables"),    
    path("news/news_statics", views.news_statics, name="news_statics"),    
]