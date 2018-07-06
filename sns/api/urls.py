from rest_framework import routers

from .views import ProfileViewSet, StatusViewSet, LikeViewSet, FollowViewSet
from .apps import app_name


router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('statuses', StatusViewSet)
router.register('likes', LikeViewSet)
router.register('follows', FollowViewSet)

urlpatterns = router.urls

