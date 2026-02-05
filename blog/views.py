from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm

from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    response_text = "Список постов:<br>"

    for post in posts:
        formatted_date = post.published_date.strftime("%d.%m.%Y %H:%M")
        response_text += f"- {post.title} {formatted_date} (автор: {post.author})\n{post.text}<br>"
    return render (request, 'blog/post_list.html', { 'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return  render(request, 'blog/post_edit.html', {'form': form})


