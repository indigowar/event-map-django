from django.urls import path

from events import views

urlpatterns = [
    path('organizer_level/', views.OrganizerLevelListAPIView.as_view()),
    path('organizer/', views.OrganizerListCreateAPIView.as_view()),
    path('organizer/<int:pk>', views.OrganizerRetrieveUpdateDestroyAPIView.as_view()),
    path('competitor/', views.CompetitorListAndCreateAPIView.as_view()),
    path('competitor/<int:pk>', views.CompetitorRetrieveUpdateDestroyAPIView.as_view()),
    path('event/', views.EventListAndCreateAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('event/<int:pk>', views.EventRetrieveUpdateDestroyAPIView.as_view()),
    path('subjects/', views.SubjectListAPIView.as_view()),
    path('founding_type/', views.FoundingTypeListCreateAPIView.as_view()),
    path('founding_type/<int:pk>', views.FoundingTypeRetrieveUpdateDestroyAPIView.as_view()),
]
