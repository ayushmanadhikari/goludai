from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def home(request):
    return render(request, 'blog/home.html')


class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
