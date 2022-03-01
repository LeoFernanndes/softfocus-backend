from rest_framework import serializers
from loss_communications.models import ComunicacaoDePerda


class ComunicacaoDePerdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunicacaoDePerda
        fields = '__all__'