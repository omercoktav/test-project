from django.urls import path
from .views import (EventCreateAPIView,
                    EventListAPIView,
                    EventUpdateAPIView,
                    EventDeleteAPIView,
                    EventDetailAPIView,
                    )


app_name="Event"

urlpatterns=[
    #Event
    path('create',EventCreateAPIView.as_view(),name='create'),
    path('list',EventListAPIView.as_view(),name='list'),
    path('detail/<slug>',EventDetailAPIView.as_view(),name='detail'),
    path('update/<slug>',EventUpdateAPIView.as_view(),name='update'),
    path('delete/<slug>',EventDeleteAPIView.as_view(),name='delete'),
]