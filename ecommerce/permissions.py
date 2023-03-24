from rest_framework import permissions


class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class IsOwner(permissions.BasePermission):
    message = "You aren't the owner of this post"

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id