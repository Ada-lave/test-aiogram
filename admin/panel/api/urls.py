from rest_framework import routers
from .views import TelegramUserViewSet, ProjectViewSet, TagViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', TelegramUserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
