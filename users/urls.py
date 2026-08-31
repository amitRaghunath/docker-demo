from rest_framework.routers import DefaultRouter

from .views import UserViewSet
from rest_framework_extensions.routers import ExtendedDefaultRouter


router = ExtendedDefaultRouter(trailing_slash=False)

router.register("users", UserViewSet, basename="users")

urlpatterns = router.urls