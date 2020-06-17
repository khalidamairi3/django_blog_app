from django.urls import path

from .views import postlist,detail

urlpatterns=[
    path("",postlist,name="postlist"),
    path("post/<int:post_id>",detail,name="detail")
]
