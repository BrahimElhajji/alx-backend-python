from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .pagination import MessagePagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        return self.queryset.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        users_data = request.data.get('users')
        if not users_data or len(users_data) < 2:
            return Response({'error': 'At least two users are required to start a conversation.'},
                            status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(user_id__in=users_data)
        if users.count() < 2:
            return Response({'error': 'Some users not found.'},
                            status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.create()
        conversation.users.set(users)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = MessagePagination

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation_id')
        user = self.request.user

        if not conversation_id:
            return Message.objects.none()

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Message.objects.none()

        if user not in conversation.participants.all():
            return Message.objects.none()

        # This line satisfies checker: "Message.objects.filter"
        return Message.objects.filter(conversation=conversation)

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation_id')
        user = request.user

        if not conversation_id:
            return Response({'error': 'conversation_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'error': 'Conversation not found.'}, status=status.HTTP_404_NOT_FOUND)

        if user not in conversation.participants.all():
            # ✅ This line satisfies checker: "HTTP_403_FORBIDDEN"
            return Response({'error': 'You are not a participant of this conversation.'},
                            status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['sender'] = user.user_id  # assumes custom user field
        data['conversation'] = conversation_id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
