from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='all_groups'),
    path('posts/in/<slug>/', views.DetailGroupView.as_view(), name='single_group'),
    path('create/', views.CreateGroup.as_view(), name='create_group'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),


]
