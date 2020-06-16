from django.shortcuts import render
from .models import Post
from django.utils import timezone

def postlist(request):
    posts=Post.objects.filter(pub_date__lte=timezone.now()).order_by("pub_date")
    front_end_stuff={"posts":posts}
    return render(request,"index.html",front_end_stuff)




# Create your views here.
