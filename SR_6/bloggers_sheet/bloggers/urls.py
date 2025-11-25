from django.urls import path, re_path
from . import views

app_name = 'bloggers'

urlpatterns = [
    path('', views.home_page, name='home'),

    path('profiles/', views.profile_list, name='profile_list'),

    re_path(r'^profiles/(?P<blogger_slug>[a-zA-Z0-9-]+)/$', views.profile_detail, name='profile_detail'),
]