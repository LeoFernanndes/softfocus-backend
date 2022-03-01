from rest_framework import routers
from loss_communications.viewsets import ComunicaccaoDePerdaViewset

router = routers.SimpleRouter()
router.register(r"comunicaccao_de_perda", ComunicaccaoDePerdaViewset, basename="comunicacao_de_perda")

urlpatterns = []
urlpatterns += router.urls