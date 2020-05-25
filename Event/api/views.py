from Event.models import Event
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView)

from session.api.permissions import IsOwner
from .serializers import (EventUpdateCreateSerializer,
                          EventListSerializer,
                          EventDetailSerializer)
from .pagination import EventPagination


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    pagination_class = EventPagination

class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'slug'

class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateCreateSerializer
    permission_classes = (IsOwner,)

class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateCreateSerializer
    lookup_field = 'slug'
    permission_classes = (IsOwner,)


    def perform_update(self, serializer):
        serializer.save()

class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    lookup_field = 'slug'



