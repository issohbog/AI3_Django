from django.shortcuts import render, redirect, get_object_or_404

from .models import Post

from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'post/index.html')

# 게시글 등록
def create_view(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})


# 게시글 목록
def list_view(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post/list.html', {'posts': posts})

# 게시글 상세 
def read_view(request , id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post/read.html', {'post': post })

# 게시글 수정 
def update_view(request, id):
    post = get_object_or_404(Post, pk=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('read', id=post.id) 
    else:
        form = PostForm(instance=post)
        
    return render(request, 'post/update.html', {'form':form, 'post': post })