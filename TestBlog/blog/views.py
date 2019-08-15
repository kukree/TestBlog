from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


class Home:

    @staticmethod
    def list_posts(request):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})


class NewPost:

    @staticmethod
    def new_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list_posts')
        else:
            form = PostForm()
        return render(request, 'blog/new_post.html', {'form': form})

    @staticmethod
    def post_detail(request, primary_key=None):
        post = get_object_or_404(Post, pk=primary_key)
        return render(request, 'blog/post_detail.html', {'post': post})
