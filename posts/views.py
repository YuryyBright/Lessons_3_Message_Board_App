from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

class HomePageView(ListView):
    model = Posts
    template_name = 'lessons_3/home.html'

