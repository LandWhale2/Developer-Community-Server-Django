from rest_framework import routers
from posts import views as postview

#글 주소
router = routers.DefaultRouter()
router.register(r'talk', postview.TalkViewset)
router.register(r'projects', postview.ProjectViewset)
router.register(r'algorithm', postview.AlgorithmViewset)
router.register(r'skilltalk', postview.SkilltalkViewset)

#댓글 주소
router.register(r'talk/(?P<id>\d+)/comment', postview.TalkCommentViewset)
router.register(r'projects/(?P<id>\d+)/comment', postview.ProjectCommentViewset)
router.register(r'algorithm/(?P<id>\d+)/comment', postview.AlgorithmCommentViewset)
router.register(r'skilltalk/(?P<id>\d+)/comment', postview.SkilltalkCommentViewset)
# router.register(r'projects', myapp_views.ProjectsViewset)


