from django.shortcuts import render, get_object_or_404, redirect
from .models import Thoughts, Comment
from .forms import PostForm

# Create your views here.

def thoughts_list(request):
    thoughts = Thoughts.objects.all()
    return render(request, "post/index.html", {'thoughts': thoughts})

def single_thought(request,id):
    thought = get_object_or_404(Thoughts, id=id)
    comments = Comment.objects.filter(thoughts=thought)
    return render(request, "post/single.html", {'thought':thought, 'comments':comments})

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thoughts")
    return render(request, "post/post_form.html", {"form":form})

def updatePost(request, pk):
    specific_post = Thoughts.objects.get(id=pk)
    form = PostForm(instance=specific_post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=specific_post)
        if form.is_valid():
            form.save()
            return redirect("thoughts")
    return render(request, "post/post_form.html", {"form":form})

def deletePost(request, pk):
    specific_post = Thoughts.objects.get(id=pk)
    if request.method == "POST":
        specific_post.delete()
        return redirect("thoughts")
    return render(request, "post/delete.html", {"obj":specific_post})
    







