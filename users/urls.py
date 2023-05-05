from django.urls import path

from users import views

urlpatterns = [
    path('info/<int:pk>', views.UserDetailsAPIView.as_view()),
    path('register', views.RegisterUserAPIView.as_view()),
    path('grand', views.GrandPermissionAPIView.as_view())
]
