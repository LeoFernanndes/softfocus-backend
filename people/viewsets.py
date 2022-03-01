from rest_framework import viewsets, permissions
from people.models import User
from people.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()