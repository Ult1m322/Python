from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.PostListView.as_view(), name='post_list'),

    # ИСПРАВЛЕНО: name='post_details' и views.post_details
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_details,
         name='post_details'),
]