from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<slug>/', views.ProfileView.as_view(), name='profile'),
    path('user/update/', views.update_profile_info, name='edit_profile'),

]
