from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommmentForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    front_end_stuff = {"posts": posts}
    return render(request, "post-list.html", front_end_stuff)


def detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        front_end_stuff = {"post": post}
    except Exception as e:
        raise
    return render(request, "detail.html", front_end_stuff)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
        front_end_stuff = {'form': form}
    return render(request, "post-edit.html", front_end_stuff)


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        front_end_stuff = {'form': form}
    return render(request, "post-edit.html", front_end_stuff)


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(pub_date__isnull=True).order_by('-created_date')
    front_end_stuff = {"posts": posts}
    return render(request, "post-draft-list.html", front_end_stuff)


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_list')


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommmentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommmentForm()
        front_end_stuff = {'form': form}
    return render(request, "add_comment.html", front_end_stuff)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)


# Create your views here.
@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', pk=comment.post.pk)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect("/")
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})
