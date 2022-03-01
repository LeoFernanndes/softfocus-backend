from rest_framework import viewsets
from loss_communications.models import ComunicacaoDePerda
from loss_communications.serializers import ComunicacaoDePerdaSerializer


class ComunicaccaoDePerdaViewset(viewsets.ModelViewSet):
    serializer_class = ComunicacaoDePerdaSerializer
    queryset = ComunicacaoDePerda.objects.all()
