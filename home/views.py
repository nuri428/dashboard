from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
import datetime
# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    now = datetime.datetime.now()   
    context = {"current_date": now, "name": "jhkang"}
    return HttpResponse(template.render(context, request))
    # return render(request, 'main.html')