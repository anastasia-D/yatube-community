from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User

POSTS_PER_PAGE = 10


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.select_related('author', 'group')
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'posts/index.html', {'page_obj': page_obj})


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:POSTS_PER_PAGE]
    return render(request, 'posts/group_list.html', {'group': group, 'posts': posts})


def profile(request: HttpRequest, username: str) -> HttpResponse:
    author = get_object_or_404(User, username=username)
    paginator = Paginator(author.posts.select_related('author', 'group'), POSTS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(
        request, 'posts/profile.html', {'author': author, 'page_obj': page_obj},
    )


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post.objects.select_related('author', 'group'), pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', username=request.user.get_username())
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    if post.author_id != request.user.pk:
        return redirect('posts:post_detail', post_id=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/create_post.html', {'form': form, 'post': post})
