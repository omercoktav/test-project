from django.urls import path
from.views import (SessionCreateAPIView,
                   SessionUpdateAPIView,
                   SessionDeleteAPIView,
                   SessionListAPIView,
                   SessionDetailAPIView)
app_name='session'
urlpatterns=[
path('create', SessionCreateAPIView.as_view(), name='create'),
path('list', SessionListAPIView.as_view(), name='list'),
path('update/<slug>', SessionUpdateAPIView.as_view(), name='update'),
path('delete/<slug>', SessionDeleteAPIView.as_view(), name='delete'),
path('detail/<slug>', SessionDetailAPIView.as_view(), name='detail'),
]