from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='cricket')
    #LWO=Webpage.objects.get(topic_name='cricket')
    LWO=Webpage.objects.exclude(topic_name='cricket')
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all()[2::]
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date='2023-06-20')
    LAO=AccessRecord.objects.filter(date__gt='2023-06-20')
    LAO=AccessRecord.objects.filter(date__lt='2023-06-20')
    LAO=AccessRecord.objects.filter(date__gte='2023-06-20')
    LAO=AccessRecord.objects.filter(date__lte='2023-06-20')
    LAO=AccessRecord.objects.filter(date__year='2021')
    LAO=AccessRecord.objects.filter(Q(name='muni')|Q(author='abcd'))
    LAO=AccessRecord.objects.filter(Q(name='muni')&Q(author='abcd'))
    LAO=AccessRecord.objects.all()
    d={'LAO':LAO}
    return render(request,'display_access.html',d)