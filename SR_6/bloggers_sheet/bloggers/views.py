from django.shortcuts import render, redirect
from django.http import Http404
from .data import BloggerData


#main page
def home_page(request):
    context = {
        'page_title': "Головна",
        'news': BloggerData.get_news()
    }
    return render(request, 'bloggers/home.html', context)

#profiles_list page
def profile_list(request):

    bloggers_with_slug = []
    for slug, blogger in BloggerData.BLOGGERS.items():
        blogger_data = blogger.copy()
        blogger_data['slug'] = slug
        bloggers_with_slug.append(blogger_data)

    context = {
        'page_title': "Список Профілів",
        'bloggers': bloggers_with_slug
    }
    return render(request, 'bloggers/profiles_list.html', context)


#profile_detail_page
def profile_detail(request, blogger_slug):

    blogger = BloggerData.get_by_slug(blogger_slug)

    if not blogger:
        raise Http404(f"Блогер з ідентифікатором '{blogger_slug}' не знайдений.")
    blogger_data = blogger.copy()
    blogger_data['slug'] = blogger_slug

    context = {
        'page_title': f"Профіль: {blogger['name']}",
        'blogger': blogger_data
    }
    return render(request, 'bloggers/profile_detail.html', context)


#news_page
def news_page(request):

    context = {
        'page_title': "Новини",
        'news': BloggerData.get_news()
    }
    return render(request, 'bloggers/news.html', context)