from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message
from django.db.models import Prefetch

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return JsonResponse({"message": "User and related data deleted successfully."})


@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST.get("receiver_id")
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")

        receiver = User.objects.get(id=receiver_id)
        parent_message = Message.objects.get(id=parent_id) if parent_id else None

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content,
            parent_message=parent_message
        )

        return redirect("some-view-name")

    return render(request, "send_message.html")


@login_required
def conversation_view(request):
    user = request.user

    top_messages = Message.objects.filter(receiver=user, parent_message__isnull=True)\
        .select_related('sender', 'receiver')\
        .prefetch_related('replies')

    return render(request, "conversation.html", {"messages": top_messages})


@login_required
def unread_messages_view(request):
    unread_msgs = Message.unread.unread_for_user(request.user).only('id', 'content', 'timestamp', 'sender')
    return render(request, "unread_messages.html", {"messages": unread_msgs})
# Create your views here.
