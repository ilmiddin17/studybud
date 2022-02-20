from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=150)
    description=models.TextField(null=True, blank=True)
    participants=models.ManyToManyField(User, related_name='participants')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created',)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created',)

    def __str__(self) -> str:
        return self.body[:50]

