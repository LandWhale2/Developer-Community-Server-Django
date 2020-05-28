from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from posts.api import router
from users import urls
from chat import urls
from posts import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('users.urls')),
    path('', views.index),
    path('like', views.like),
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)