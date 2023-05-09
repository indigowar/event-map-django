from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission

from .serializers import UserSerializer, RegisterSerializer, OnlyIDUserSerializer


class UserDetailsAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RetrieveUserSelfInfoAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class IsSuperUser(BasePermission):
    """
    This is a permission to ensure that only superuser can do certain things
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class GrandPermissionAPIView(CreateAPIView):
    serializer_class = OnlyIDUserSerializer
    permission_classes = (IsSuperUser,)

    def create(self, request, *args, **kwargs):
        s = OnlyIDUserSerializer(data=request.body)

        if not s.is_valid():
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

        user_id = s.data.get('id')
        target = User.objects.get(pk=user_id)
        target.is_staff = True
        target.save()

        return Response(data=s.data, status=status.HTTP_202_ACCEPTED)


class DeGrandPermissionAPIView(CreateAPIView):
    serializer_class = OnlyIDUserSerializer
    permission_classes = (IsSuperUser,)

    def create(self, request, *args, **kwargs):
        s = OnlyIDUserSerializer(data=request.body)

        if not s.is_valid():
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

        user_id = s.data.get('id')
        target = User.objects.get(pk=user_id)
        if not target.is_staff:
            return Response(data=request.body, status=status.HTTP_400_BAD_REQUEST)
        target.is_staff = False
        target.save()

        return Response(data=s.data, status=status.HTTP_202_ACCEPTED)


class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
