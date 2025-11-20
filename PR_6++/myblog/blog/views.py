from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


# ИСПРАВЛЕНО: функция называется post_details
def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # ИСПРАВЛЕНО: путь к шаблону 'blog/post/details.html'
    return render(request, 'blog/post/details.html', {'post': post})