from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
from .models import NewsArticle

import datetime
# Create your views here.
def index(request):
    template = loader.get_template('main.html')    
    now = datetime.datetime.now().date()
    
    # yesterday = now - datetime.timedelta(days=1)
    # before_week = now - datetime.timedelta(days=7)
    # yesterday_count = NewsArticle.objects.filter(created_date__range=(yesterday,now)).count()
    # today_count = NewsArticle.objects.filter(created_date__gt=now).count()
    # recent_week_count = NewsArticle.objects.filter(created_date__gt=before_week).count()
    # total_count = NewsArticle.objects.all().count() 
    
    yesterday_count = 0 
    today_count = 0 
    recent_week_count = 0 
    total_count = 0 
    
    context = {
        "yesterday_count": "{:,}".format(yesterday_count),
        "today_count": "{:,}".format(today_count),
        "weekly_sum": "{:,}".format(recent_week_count), 
        "total_count": "{:,}".format(total_count)
        }
    return HttpResponse(template.render(context, request))

