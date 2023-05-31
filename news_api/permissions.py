from rest_framework import permissions


class IsPublisherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.publisher == request.user


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class CanCreateNews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        return False


class CanUpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated and obj == request.user) or request.user.is_superuser:
            return True
        return False
