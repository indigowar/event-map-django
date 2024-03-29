from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/', include('events.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/user/', include('users.urls')),

    path('accounts/', include('rest_registration.api.urls')),

    path("admin/", admin.site.urls),
]
