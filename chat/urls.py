from django.urls import path
from . import views
urlpatterns = [
    # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users/', views.user_list, name='user-list'),
]