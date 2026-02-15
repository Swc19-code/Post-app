from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import BlogForm



from . models import Blog, Categories
from django.core.paginator import Paginator




def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            login(request, user)
            return redirect('blog_list')
        else:
            messages.error(request, "Please correct the error below")
    else:
        form = UserCreationForm()
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    return render(request, "register.html", { "form" : form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

def index(request):
    return render(request, "index.html",)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")

@login_required(login_url='login')
def blog_list(request):
    posts = Blog.objects.all().order_by("-id")

    search_query = request.GET.get("search")
    category_id = request.GET.get("category")
    if search_query:
        posts = posts.filter(
            Q(title__icontains = search_query) |
            Q(content__icontains = search_query)
        )
    if category_id:
        posts = posts.filter(category_id=category_id)

    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Categories.objects.all()

    return render(request, "blog_list.html", {
        "page_obj": page_obj,
        "categories": categories,
    })

@login_required(login_url='login')
def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    related_posts = Blog.objects.filter(category=post.category).exclude(pk=pk)[:3]

    return render(request,"blog_details.html", {
        "post": post,
        "related_posts": related_posts
    })

@login_required(login_url='login')
def my_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    related_posts = Blog.objects.filter(author = request.user,category=post.category).exclude(pk=pk)[:3]

    return render(request,"my_post_view.html", {
        "post": post,
        "related_posts": related_posts
    })

@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST ,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully")
            return redirect('my_post_view', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, "create_post.html", { "form": form})

@login_required(login_url='login')
def my_posts(request):
    posts = Blog.objects.filter(author = request.user).order_by("-id")

    search_query = request.GET.get("search")
    category_id = request.GET.get("category")
    if search_query:
        posts = posts.filter(
            Q(title__icontains = search_query) |
            Q(content__icontains = search_query)
        )
    if category_id:
        posts = posts.filter(category_id=category_id)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Categories.objects.all()

    return render(request, "my_posts.html", {
        "page_obj": page_obj,
        "categories": categories,
    })

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk, author=request.user)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("my_posts")
    else:
        form = BlogForm(instance=post)
    return render(request, "create_post.html", {"form": form})

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        return redirect("my_posts")

    return redirect("my_posts")