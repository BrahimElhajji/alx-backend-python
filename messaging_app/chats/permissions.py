
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow users to access only their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Adjust the logic depending on your model (e.g., obj.user, obj.sender, obj.owner)
        return obj.user == request.user
