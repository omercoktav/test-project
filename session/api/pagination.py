from rest_framework.pagination import PageNumberPagination

class SessionPagination(PageNumberPagination):
    page_size = 2