from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import NewsArticle
from .models import WeekOfYear, DayOfWeek
from django.db.models import Count
# Create your views here.
def news_tables(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: 2일 이내 뉴스 중에서 최근 10개의 뉴스 반환
    """
    template = loader.get_template('./news/news_tables.html')
    now = datetime.datetime.now().date()
    the_day_before_yesterday = now - datetime.timedelta(days=2)
    news_list = NewsArticle.objects.filter(created_date__gt=the_day_before_yesterday).order_by('-id')[:10]
    context = {
        'news_list': news_list
    }
    return HttpResponse(template.render(context, request))
    
    
def news_statics(request):
    """뉴스 통계 반환

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    template = loader.get_template('./news/news_statics.html')
    now = datetime.datetime.now().date()
    current_woy = now.isocalendar()[1]
    the_day_before_7days = now - datetime.timedelta(days=7)
    
    recent_week = NewsArticle.objects.annotate(  
            dow=DayOfWeek('created_date')
        ).values('dow').annotate(
            count=Count('created_date')
        ).filter(created_date__gt=the_day_before_7days).order_by('dow').values('dow','count')
    recent_week = {item['dow']:item['count'] for item in recent_week}
    
    current_week = NewsArticle.objects.annotate(  
            woy=WeekOfYear('created_date')
        ).values('woy').annotate(  
            dow=DayOfWeek('created_date')
        ).values('dow').annotate(
            count=Count('created_date')
        ).filter(woy=current_woy).order_by('dow').values('dow','count')
    current_week = {item['dow']:item['count'] for item in current_week}
        
    previsous_week = NewsArticle.objects.annotate(  
            woy=WeekOfYear('created_date')
        ).values('woy').annotate(  
            dow=DayOfWeek('created_date')
        ).values('dow').annotate(
            count=Count('created_date')
        ).filter(woy=(current_woy-1)).order_by('dow').values('dow','count')
    previsous_week = {item['dow']:item['count'] for item in previsous_week}
    
    context = {
        'recent_week':list(recent_week.values()),
        'current_week':list(current_week.values()),
        'previsous_week':list(previsous_week.values())
    }
    
    return HttpResponse(template.render(context, request))
    