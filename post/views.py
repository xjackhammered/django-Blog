from django.shortcuts import render, get_object_or_404
from .models import Thoughts, Comment

# Create your views here.

def thoughts_list(request):
    thoughts = Thoughts.objects.all()
    return render(request, "post/index.html", {'thoughts': thoughts})

def single_thought(request,id):
    thought = get_object_or_404(Thoughts, id=id)
    comments = Comment.objects.filter(thoughts=thought)
    return render(request, "post/single.html", {'thought':thought, 'comments':comments})