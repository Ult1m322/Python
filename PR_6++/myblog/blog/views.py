from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    # Получаем пост по дате и слагу [cite: 398]
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)

    return render(request, 'blog/post/detail.html', {'post': post})