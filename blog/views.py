from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

def debug_view(request):
    obj = Post.objects.first()
    return render(request, 'debug.html', {'object': obj})