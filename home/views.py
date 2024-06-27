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
    yesterday_count = NewsArticle.objects.filter(created_date__range=(yesterday,now)).count()
    today_count = NewsArticle.objects.filter(created_date__gt=now).count()
    
    context = {
        "yesterday_count": "{:,}".format(yesterday_count),
        "today_count": "{:,}".format(today_count)
        }
    return HttpResponse(template.render(context, request))
    # return render(request, 'main.html')