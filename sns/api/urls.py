from rest_framework import routers

from .views import ProfileViewSet, StatusViewSet
from .apps import app_name


router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('statuses', StatusViewSet)

