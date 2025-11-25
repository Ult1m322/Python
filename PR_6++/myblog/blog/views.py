from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail  # <--- НОВЫЙ ИМПОРТ
from .models import Post
from .forms import EmailPostForm  # <--- НОВЫЙ ИМПОРТ


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/details.html', {'post': post})


# <--- НОВАЯ ФУНКЦИЯ
def post_share(request, post_id):
    # Получить пост по id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        # Форма была отправлена
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы прошли валидацию
            cd = form.cleaned_data
            # Ссылка на пост
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}'s comments: {cd['comments']}"

            # Отправка письма (настройки в settings.py)
            send_mail(subject, message, 'mr.ultimatrix@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})