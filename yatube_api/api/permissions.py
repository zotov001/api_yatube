from rest_framework import permissions


class UserIsAuthor(permissions.BasePermission):
    message = 'У вас недостаточно прав для совершения действия'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
