from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect 

def news_redirect(request):
    return redirect('bloggers:home') 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('news/', news_redirect),

    path('', include('bloggers.urls')),
]