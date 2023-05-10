from rest_framework import permissions
from rest_framework.permissions import BasePermission


class MoviePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Проверяем, что пользователь является администратором
        return request.user and request.user.is_superuser


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Проверяем, что пользователь является администратором
        return request.user and request.user.is_superuser


class IsAuthorOrAllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated:
            return True
        return False
