from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import SignUpView
from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('profile/', include('accounts.urls', namespace='profile')),
    path('', HomeView.as_view(), name='home'),


    path('group/', include('groups.urls', namespace="groups")),
    path('post/', include('posts.urls', namespace="posts")),
    path('search/', include('searches.urls', namespace="search")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
