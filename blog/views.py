from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm

def postlist(request):
    posts=Post.objects.filter(pub_date__lte=timezone.now()).order_by("pub_date")
    front_end_stuff={"posts":posts}
    return render(request,"index.html",front_end_stuff)
def detail(request,post_id):
    try:
        post = Post.objects.get(pk=post_id)
        front_end_stuff={"post":post}
    except Exception as e:
        raise
    return render(request,"detail.html",front_end_stuff)


def createpost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.pub_date=timezone.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form =PostForm()
        front_end_stuff={'form':form}
    return render(request,"post-edit.html",front_end_stuff)

def edit(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.pub_date=timezone.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form =PostForm(instance=post)
        front_end_stuff={'form':form}
    return render(request,"post-edit.html",front_end_stuff)



# Create your views here.
