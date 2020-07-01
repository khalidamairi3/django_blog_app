from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm,CommmentForm
from django.contrib.auth.decorators import login_required
def postlist(request):
    posts=Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    front_end_stuff={"posts":posts}
    return render(request,"index.html",front_end_stuff)
def detail(request,post_id):
    try:
        post = Post.objects.get(pk=post_id)
        front_end_stuff={"post":post}
    except Exception as e:
        raise
    return render(request,"detail.html",front_end_stuff)

@login_required
def createpost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form =PostForm()
        front_end_stuff={'form':form}
    return render(request,"post-edit.html",front_end_stuff)
    
@login_required
def edit(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form =PostForm(instance=post)
        front_end_stuff={'form':form}
    return render(request,"post-edit.html",front_end_stuff)


@login_required
def post_draft_list(request):
    posts=Post.objects.filter(pub_date__isnull=True).order_by('-created_date')
    front_end_stuff={"posts":posts}
    return render(request,"post-draft-list.html",front_end_stuff)


@login_required
def publish_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('postlist')



@login_required
def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommmentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return redirect('detail',post_id=post.pk)
    else:
        form =CommmentForm()
        front_end_stuff={'form':form}
    return render(request,"add_comment.html",front_end_stuff)



# Create your views here.
