
from rest_framework import routers
from people.viewsets import UserViewset

router = routers.SimpleRouter()
router.register(r"users", UserViewset, basename="user")

urlpatterns = []
urlpatterns += router.urls