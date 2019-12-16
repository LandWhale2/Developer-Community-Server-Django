from rest_framework import routers
from posts import views as postview

# 글 전용 주소
router = routers.DefaultRouter()
router.register(r'talk', postview.TalkViewset)
router.register(r'projects', postview.ProjectViewset)
router.register(r'algorithm', postview.AlgorithmViewset)
router.register(r'skilltalk', postview.SkilltalkViewset)

# router.register(r'projects', myapp_views.ProjectsViewset)
