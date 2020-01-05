from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostsList.as_view(), name='all_posts'),
    path('by/<username>/', views.UserPostsList.as_view(), name='user_posts'),
    path('by/<username>/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/post/', views.PostCreateView.as_view(), name='post_create'),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='delete_post'),

    ]
