from django.contrib.auth.models import User, Permission, Group

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.views import APIView

from .serializers import UserSerializer, RegisterSerializer, OnlyIDUserSerializer


class UserDetailsAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


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


# class GrandPermissionsAPIView(CreateAPIView):
#     serializer_class = OnlyIDUserSerializer()
#     permission_classes = (IsSuperUser,)
#
#     def post(self, request, *args, **kwargs):
#         parsed = OnlyIDUserSerializer(data=request.body)
#         if parsed.is_valid(raise_exception=True):
#             user_id = parsed.data.get('id')
#             target = User.objects.get(pk=user_id)
#
#             return Response(data=parsed.data, status=status.HTTP_200_OK)
#         return Response(parsed.errors, status=status.HTTP_400_BAD_REQUEST)
