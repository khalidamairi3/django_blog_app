from django.urls import path
from . import views


urlpatterns=[
    path("",views.postlist,name="postlist"),
    path("post/<int:post_id>",views.detail,name="detail"),
    path("create/",views.createpost,name="createpost"),
    path("post/<int:post_id>/edit",views.edit,name="edit"),
    path("post-draft-list",views.post_draft_list,name="post-draft-list"),
    path("post/<int:pk>/publish",views.publish_post,name="publish_post"),
    path("post/<int:pk>/add_comment",views.add_comment,name="add_comment"),
    path("comment/<int:pk>/comment_remove",views.comment_remove,name="comment_remove"),
    path("comment/<int:pk>/approve_comment",views.approve_comment,name="approve_comment"),
    path("post/<int:pk>/delete",views.delete_post,name="delete_post"),
    
]
