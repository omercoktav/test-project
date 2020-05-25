from rest_framework.generics import (CreateAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from.serializer import (SessionCreateUpdateSerializer,
                        SessionListSerializer,
                        SessionDetailSerializer)
from .pagination import SessionPagination
from session.models import Session
class SessionCreateAPIView(CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionCreateUpdateSerializer
    permission_classes = (IsOwner,)

class SessionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = (IsOwner,)

    def perform_update(self, serializer):
        serializer.save()

class SessionDeleteAPIView(DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = (IsOwner,)


class SessionListAPIView(ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionListSerializer
    pagination_class = SessionPagination

class SessionDetailAPIView(RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionDetailSerializer
    lookup_field = 'slug'
