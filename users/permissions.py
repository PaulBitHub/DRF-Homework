from rest_framework.permissions import BasePermission

class IsModer(BasePermission):
    """Проверяет, является ли пользователь модератором"""

    def has_permission(self, request, view):
        # Сначала проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name="moders").exists()


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта"""

    def has_object_permission(self, request, view, obj):
        # Сначала проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return False
        return obj.owner == request.user
