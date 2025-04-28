from django.urls import path
from . import views 

urlpatterns = [
    path("home/", views.thoughts_list, name="thoughts"),
    path("thought/<int:id>", views.single_thought, name="single"),
]
