from django.shortcuts import get_object_or_404, redirect, render
from django.template import context
from django.contrib.auth.models import User
from main.forms import MessageForm, RoomCreateForm
from .models import Room,Message,Topic
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
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
        'top_hosts':top_hosts,
        
    }
    return render(request, 'main/home.html',context)

def create_room(request):
    if request.method=='POST':
        form=RoomCreateForm(request.POST)
        participant=User.objects.get(id=request.user.id)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            room.participants.add(participant)
            return redirect('main:home')
    else:
        form=RoomCreateForm()
    return render(request, 'main/room_create.html', {'form':form})

def room_detail(request, room_id):
    msg_form=MessageForm()
    room=get_object_or_404(Room, id=room_id)
    messages=Message.objects.filter(room=room)
    count=room.participants.all().count()
    participants=room.participants.all()[:10]
    if request.method=='POST' and 'joinbutton' in request.POST:
        participant=User.objects.get(id=request.user.id)
        room.participants.add(participant)
        return HttpResponseRedirect(request.path_info)
    if request.method=='POST' and 'messageCreate' in request.POST:
        msg_form=MessageForm(request.POST)
        msg=msg_form.save(commit=False)
        msg.user=request.user
        msg.room=room
        msg.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'main/room_detail.html', {'room':room, 'messages':messages, 'count':count, 'msg_form':msg_form, 'participants':participants})