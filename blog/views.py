from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm


# Create your views here.

# def index(request): 
#     return HttpResponse("<h1> Welcome to our Website </h1>")

def home(request):
     posts = Post.objects.all()
     return render(request, 'home.html', {'posts' : posts})


def about(request):
    return render(request, 'about.html')


def delete(request, id):
     # id = request.GET.get('id')    
     post = Post.objects.get(id=id)
     post.delete()
     return HttpResponseRedirect('/')

def createPost(request):
     if request.method == "POST":
          form = PostForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')
     else:
          form = PostForm()
          return render(request, "insert.html",{'form': form})

def single(request, id):
     post = Post.objects.get(id=id)
     return render(request, "single.html",{'post': post})
