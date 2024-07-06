from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
from .models import NewsArticle

import datetime
# Create your views here.
def index(request):
    template = loader.get_template('main.html')    
    now = datetime.datetime.now().date()
    
    yesterday = now - datetime.timedelta(days=1)
    before_week = now - datetime.timedelta(days=7)
    yesterday_count = NewsArticle.objects.filter(created_date__range=(yesterday,now)).count()
    today_count = NewsArticle.objects.filter(created_date__gt=now).count()
    recent_week_count = NewsArticle.objects.filter(created_date__gt=before_week).count()
    total_count = NewsArticle.objects.all().count() 
    
    context = {
        "yesterday_count": "{:,}".format(yesterday_count),
        "today_count": "{:,}".format(today_count),
        "weekly_sum": "{:,}".format(recent_week_count), 
        "total_count": "{:,}".format(total_count)
        }
    return HttpResponse(template.render(context, request))
    # return render(request, 'main.html')
    
def news_tables(request):
    template = loader.get_template('./pages/news_tables.html')
    now = datetime.datetime.now().date()
    the_day_before_yesterday = now - datetime.timedelta(days=2)
    news_list = NewsArticle.objects.filter(created_date__gt=the_day_before_yesterday).order_by('-id')[:10]
    context = {
        'news_list': news_list
    }
    return HttpResponse(template.render(context, request))
    