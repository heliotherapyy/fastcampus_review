from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


@login_required
def index(request):
    post_list = Post.objects.all()
    return render(request, 'miniblog/index.html', {
        'post_list': post_list,
    })


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'miniblog/detail.html', {
        'post': post,
    })





