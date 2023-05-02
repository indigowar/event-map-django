from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import UserSerializer, RegisterSerializer


class UserDetailsAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
