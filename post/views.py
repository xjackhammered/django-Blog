from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Thoughts, Comment, Category
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("thoughts")
        else:
            messages.error(request, "Username or password does not exist.")
    
    return render(request, "post/login_register.html", {"page":page})

def logoutUser(request):
    logout(request)
    return redirect("thoughts")


def thoughts_list(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    thoughts = Thoughts.objects.filter(Q(category__name__icontains=q)|Q(title__icontains=q))
    categories = Category.objects.all()
    thought_count = thoughts.count()

    return render(request, "post/index.html", {'thoughts': thoughts, 'categories':categories, "thought_count":thought_count})

def single_thought(request,id):
    thought = get_object_or_404(Thoughts, id=id)
    comments = Comment.objects.filter(thoughts=thought)
    return render(request, "post/single.html", {'thought':thought, 'comments':comments})

@login_required(login_url="login")
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thoughts")
    return render(request, "post/post_form.html", {"form":form})

@login_required(login_url="login")
def updatePost(request, pk):
    specific_post = Thoughts.objects.get(id=pk)
    form = PostForm(instance=specific_post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=specific_post)
        if form.is_valid():
            form.save()
            return redirect("thoughts")
    return render(request, "post/post_form.html", {"form":form})

@login_required(login_url="login")
def deletePost(request, pk):
    specific_post = Thoughts.objects.get(id=pk)
    if request.method == "POST":
        specific_post.delete()
        return redirect("thoughts")
    return render(request, "post/delete.html", {"obj":specific_post})
    







