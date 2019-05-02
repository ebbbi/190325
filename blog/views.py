from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
def home(request):
    posts=Post.objects.all
    return render(request, 'home.html', {'posts_list' : posts})
    
def new(request):
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request, 'new.html', {'form':form})
    
