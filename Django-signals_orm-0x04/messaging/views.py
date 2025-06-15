from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return JsonResponse({"message": "User and related data deleted successfully."})

# Create your views here.
