from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

app_name = 'user'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('signin', views.SignIn.as_view(), name='signin'),
    path('check/<str:email>', views.EmailCheckView.as_view(), name='check'),
    path('activate/<str:uidb64>/<str:token>', views.UserActivate.as_view(), name="activate"),
    path('userupdate', views.UserDetail.as_view(), name="userupdate"),
]

urlpatterns = format_suffix_patterns(urlpatterns)