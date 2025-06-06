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

def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("thoughts")
        else:
            messages.error(request, "An error has occured during registration.")
    return render(request, "post/login_register.html", {"form": form})


def thoughts_list(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    thoughts = Thoughts.objects.filter(Q(category__name__icontains=q)|Q(title__icontains=q))
    categories = Category.objects.all()
    thought_count = thoughts.count()
    comments = Comment.objects.all()

    return render(request, "post/index.html", {'thoughts': thoughts, 'categories':categories, "thought_count": thought_count, "comments":comments})

def single_thought(request,id):
    thought = Thoughts.objects.get(id=id)
    comments = thought.comment_set.all()

    if request.method == "POST":
        comment = Comment.objects.create (
            user = request.user,
            thoughts = thought,
            content = request.POST.get('content')
        )
        return redirect("single",id=thought.id)
    
    return render(request, "post/single.html", {'thought':thought, 'comments':comments})

@login_required(login_url="login")
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            thoughts = form.save(commit=False)
            thoughts.host = request.user
            thoughts.save()
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
    

@login_required(login_url="login")
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == "POST":
        comment.delete()
        return redirect("thoughts")
    return render(request, "post/delete.html", {"obj":comment})

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    thoughts = user.thoughts_set.all()
    comments = user.comment_set.all()
    categories = Category.objects.all()

    return render(request, "post/profile.html", {"user": user, "thoughts":thoughts, "comments":comments, "categories":categories})



