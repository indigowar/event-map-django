from django.urls import path

from events import views

urlpatterns = [
    path('organizer_level/', views.OrganizerLevelListAPIView.as_view()),
    path('organizer/', views.OrganizerListCreateAPIView.as_view()),
    path('organizer/<int:pk>', views.OrganizerRetrieveUpdateDestroyAPIView.as_view()),
    path('competitor/', views.CompetitorListAPIView.as_view()),
    path('founding_type/', views.FoundingTypeListAPIView.as_view()),
    path('event/', views.EventListAndCreateAPIView.as_view()),
    path('event/<int:pk>', views.EventRetrieveUpdateDestroyAPIView.as_view()),
    path('filtration/', views.EventFilterListAPIView.as_view())
]
