from rest_framework import routers

from .views import ProfileViewSet, StatusViewSet, LikeViewSet
from .apps import app_name


router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('statuses', StatusViewSet)
router.register('likes', LikeViewSet)

urlpatterns = router.urls

