from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse
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
    LAO=AccessRecord.objects.filter(date__month='07')
    LAO=AccessRecord.objects.filter(date__day='13')
    LAO=AccessRecord.objects.filter(author__regex='m\w+')
    LAO=AccessRecord.objects.filter(author__in=['muni','abc'])
    LAO=AccessRecord.objects.filter(author__startswith='m')
    LAO=AccessRecord.objects.filter(author__endswith='d')
    LAO=AccessRecord.objects.filter(author__contains='a')
    LAO=AccessRecord.objects.filter(date__year__gt='2021')

    d={'LAO':LAO}
    return render(request,'display_access.html',d)


def update_webpages(request):
    # Webpage.objects.filter(name='dhoni').update(url='http://msd.com')
    # Webpage.objects.filter(topic_name='cricket').update(url='http://indiateam.com')
    # Webpage.objects.filter(name='alekhya').update(url='http://alekhya.com')
    # Webpage.objects.filter(name='dhoni').update(topic_name='hockey')
    # Webpage.objects.filter(name='dhoni').update(topic_name='rugby')


    #Webpage.objects.update_or_create(name='dhoni',defaults={'url':'http://abc.com'})
    # Webpage.objects.update_or_create(topic_name='rugby',defaults={'url':'http://rugby.com'})
    cto=Topic.objects.get(topic_name='cricket')
    Webpage.objects.update_or_create(name='abc',defaults={'topic_name':cto})
    Webpage.objects.update_or_create(name='mounika',defaults={'topic_name':cto,'url':'http://mouni.com'})
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
def delete_webpages(request):
    Webpage.objects.filter(name='virat').delete()
    Webpage.objects.filter(topic_name='cricket').delete()

    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
