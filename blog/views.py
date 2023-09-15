from django.shortcuts import render
from django.core.paginator import Paginator ,EmptyPage , PageNotAnInteger
from .models import Post



# Create your views here.
def post_list(request):
    posts = Post.published.all()
    # sen data to temp
    per_page = 10
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page')

    try:
        posts = Paginator.page(page)
    except PageNotAnInteger:
        posts = Paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    post = Post.published.get(id=id) 
    return render(request, 'blog/post/detail.html', {'post': post})
