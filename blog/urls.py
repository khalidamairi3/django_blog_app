from django.urls import path

from . import views

urlpatterns=[
    path("",views.postlist,name="postlist"),
    path("post/<int:post_id>",views.detail,name="detail"),
    path("create/",views.createpost,name="createpost"),
]
