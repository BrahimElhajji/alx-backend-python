
from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow access only to users who are participants of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming obj is a Message or Conversation with a 'conversation' field that has 'participants'
        user = request.user

        # obj could be a Message or a Conversation
        if hasattr(obj, 'conversation'):
            return user in obj.conversation.participants.all()
        elif hasattr(obj, 'participants'):
            return user in obj.participants.all()

        return False
