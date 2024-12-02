from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'post.html', {'posts': posts})
