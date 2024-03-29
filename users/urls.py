from django.urls import path

from users import views

urlpatterns = [
    path('about/<int:pk>', views.UserDetailsAPIView.as_view()),
    path('info', views.RetrieveUserSelfInfoAPIView.as_view()),
    path('register', views.RegisterUserAPIView.as_view()),
    path('grand/<int:user_id>/', views.PromoteToStaffAPIView.as_view(), name='promote_user_to_staff'),
    path('degrand/<int:user_id>/', views.DeGrandPermissionAPIView.as_view()),
    path('list', views.ListUserAPIView.as_view()),
]
