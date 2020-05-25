from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = "Not an owner."

    def has_object_permission(self, request, view, Event):
        return request.user.id == Event.user.id
