from rest_framework import routers
from posts import views as myapp_views

router = routers.DefaultRouter()
router.register(r'talk', myapp_views.TalkViewset)
router.register(r'projects', myapp_views.ProjectViewset)
# router.register(r'projects', myapp_views.ProjectsViewset)
