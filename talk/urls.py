from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from talk import views


urlpatterns = [
    url(r'^$', views.TalkList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.TalkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)