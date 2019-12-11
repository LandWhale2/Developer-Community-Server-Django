from rest_framework import routers
from posts import views as myapp_views

# 글 전용 주소
router = routers.DefaultRouter()
router.register(r'talk', myapp_views.TalkViewset)
router.register(r'projects', myapp_views.ProjectViewset)
router.register(r'algorithm', myapp_views.AlgorithmViewset)
router.register(r'skilltalk', myapp_views.SkilltalkViewset)

# router.register(r'projects', myapp_views.ProjectsViewset)
