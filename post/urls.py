from django.urls import path
from . import views 

urlpatterns = [
    path("home/", views.thoughts_list, name="thoughts"),
    path("login/", views.loginPage, name="login"),
    path("register/",views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/<int:pk>/",views.userProfile, name="profile"),
    path("thought/<int:id>/", views.single_thought, name="single"),
    path("create-post/", views.createPost, name="create-post"),
    path("update-post/<int:pk>/", views.updatePost, name="update-post"),
    path("delete-post/<int:pk>/", views.deletePost, name="delete-post"),
    path("delete-comment/<int:pk>/", views.deleteComment, name="delete-comment")
]
