from django.urls import path

from . import views

urlpatterns=[
    path("",views.postlist,name="postlist"),
    path("post/<int:post_id>",views.detail,name="detail"),
    path("create/",views.createpost,name="createpost"),
    path("post/<int:post_id>/edit",views.edit,name="edit"),
    path("post-draft-list",views.post_draft_list,name="post-draft-list"),
    path("post/<int:pk>/publish",views.publish_post,name="publish_post"),
]
