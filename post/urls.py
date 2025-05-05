from django.urls import path
from . import views 

urlpatterns = [
    path("home/", views.thoughts_list, name="thoughts"),
    path("login/", views.loginPage, name="login"),
    path("thought/<int:id>", views.single_thought, name="single"),
    path("create-post/", views.createPost, name="create-post"),
    path("update-post/<int:pk>/", views.updatePost, name="update-post"),
    path("delete-post/<int:pk>/", views.deletePost, name="delete-post"),
]
