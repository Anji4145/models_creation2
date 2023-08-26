from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Insert_Topic(request):
    tn = input('Enter topic_name: ')
    td = Topic.objects.get_or_create(topic_name = tn)[0]
    td.save()
    return HttpResponse('data is entred')
def Insert_Webpage(request):
    wo = input('Enter topic_name: ')
    wp = Webpage.objects.get(topic_name = wo)
    n = input('Enter name: ')
    u = input('Enter url_link: ')
    wa = Webpage.objects.get_or_create(topic_name=wp,name=n,url=u)
    wa.save()
    return HttpResponse('data is entred')

def display_topic(request):
    qsto = Topic.objects.all()
    d ={'qsto':qsto}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    wpqs = Webpage.objects.all()
    d ={'wpqs':wpqs}
    return render(request,'display_webpage.html',d)

def display_AccessRecords(request):
    arqs = AccessRecord.objects.all()
    d ={'arqs':arqs}
    return render(request,'display_AccessRecords.html',d)

def Insert_accessrecord(request):
    nm = input('enter name : ')
    dt = input('enter date : ')
    au = input('enter author : ')
    em = input('enter email : ')
    wo = Webpage.objects.get(name=nm)
    ao = AccessRecord.objects.get_or_create(name=nm,date=dt,author=au,email=em)
    ao.save()
    arqs = AccessRecord.objects.all()
    d ={'arqs':arqs}
    return render(request,'display_AccessRecords.html',d)
