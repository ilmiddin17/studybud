from django.urls import path
from .views import home, ex

app_name='main'
urlpatterns=[
    path('', home, name='home'),
    path('ex/', ex, name='ex')
]