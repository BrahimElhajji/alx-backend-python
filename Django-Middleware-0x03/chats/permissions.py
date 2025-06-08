
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants to access or modify messages.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Check if user is authenticated
        if not user or not user.is_authenticated:
            return False

        # Handle object with a conversation
        if hasattr(obj, 'conversation'):
            participants = obj.conversation.participants.all()
        elif hasattr(obj, 'participants'):
            participants = obj.participants.all()
        else:
            return False

        # Allow only participants to do PUT/PATCH/DELETE
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return user in participants

        # Read-only access for participants
        return user in participants

