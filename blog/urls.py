from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create/", views.create_post, name="create_post"),
    path("post/<int:pk>", views.detail, name="detail"),
    path("post/<int:pk>/edit", views.edit_post, name="edit_post"),
    path("post/<int:pk>/publish", views.publish_post, name="publish_post"),
    path("post/<int:pk>/add_comment", views.add_comment, name="add_comment"),
    path("post/<int:pk>/delete", views.delete_post, name="delete_post"),
    path("post-draft-list", views.post_draft_list, name="post-draft-list"),
    path("comment/<int:pk>/comment_remove", views.comment_remove, name="comment_remove"),
    path("comment/<int:pk>/approve_comment", views.approve_comment, name="approve_comment"),
    path("signup/", views.signup, name='signup')

]
