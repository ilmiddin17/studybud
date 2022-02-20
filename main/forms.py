from pyexpat import model
from django import forms
from .models import Message, Room, Topic

class RoomCreateForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['topic', 'name', 'description']

    

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['body']