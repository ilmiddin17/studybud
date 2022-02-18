from django.shortcuts import render
from django.template import context
from .models import Room,Message,Topic
from django.db.models import Count
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    rooms_count=rooms.count()
    topics=Topic.objects.annotate(top_topics=Count('room')).order_by('-top_topics')[:10]
    top_hosts=User.objects.annotate(num_albums=Count('room')).order_by('-num_albums')[:5]
    context={
        'rooms':rooms,
        'topics':topics,
        'rooms_count':rooms_count,
        'top_hosts':top_hosts
    }
    return render(request, 'main/home.html',context)

def ex(request):
    return render(request, 'main/ex.html')