from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.list import ListView


def world(request):
    return HttpResponse("World is amazing, you received amazing chance to be in this world")

def post_view(request):
    context = {}
    context['all_posts'] = Post.objects.all()
    return render(request, "all_posts_func.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'all_posts_class.html'
