from django.urls import path

from events import views

urlpatterns = [
    path('organizer/', views.OrganizerViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('organizer/<int:pk>', views.OrganizerViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),

    path('organizer_level/', views.OrganizerLevelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('organizer_level/<int:pk>', views.OrganizerLevelViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),

    path('competitor/', views.CompetitorViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('competitor/<int:pk>', views.CompetitorViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),

    path('founding_type/', views.FoundingTypeViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('founding_type/<int:pk>', views.FoundingTypeViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),

    path('event_minimal/', views.MinimalEventListAPIView.as_view({'get': 'list'})),
    path('event_print/', views.EventForPrintingListAPIView.as_view({'get': 'list'})),

    path('subjects/', views.SubjectListAPIView.as_view()),
]
