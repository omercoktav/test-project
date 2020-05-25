from rest_framework import permissions

from session.models import Session


class IsOwner(permissions.BasePermission):
    message = "Not an owner."

    def has_object_permission(self, request, view, Session):
        return request.user.id == Session.user.id
