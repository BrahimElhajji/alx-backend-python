
from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'phone_number']


class MessageSerializer(serializers.ModelSerializer):
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'created_at']


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'users', 'messages']

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    def validate_users(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("A conversation must include at least two users.")
        return value
