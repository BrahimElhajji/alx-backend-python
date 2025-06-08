# chats/middleware.py

import time
from datetime import datetime, time, timedelta
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        with open("requests.log", "a") as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")
        return self.get_response(request)


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time(18, 0, 0)
        end_time = time(21, 0, 0)
        current_time = datetime.now().time()

        if not (start_time <= current_time <= end_time):
            return HttpResponseForbidden("Chat access is only allowed between 6PM and 9PM.")

        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store IP addresses and their message timestamps
        self.ip_message_times = {}

    def __call__(self, request):
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Initialize or clean outdated timestamps
            if ip not in self.ip_message_times:
                self.ip_message_times[ip] = []
            else:
                # Remove timestamps older than 1 minute
                one_minute_ago = now - timedelta(minutes=1)
                self.ip_message_times[ip] = [t for t in self.ip_message_times[ip] if t > one_minute_ago]

            # Check if limit exceeded
            if len(self.ip_message_times[ip]) >= 5:
                return HttpResponseForbidden("Message limit exceeded. Please wait before sending more messages.")

            # Record current message time
            self.ip_message_times[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        # Get IP address from X-Forwarded-For header or remote addr
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        
        # If user is not authenticated or role is missing, deny access
        if not user or not user.is_authenticated:
            return HttpResponseForbidden("Access denied: User not authenticated.")
        
        # Assuming your User model has a 'role' attribute
        user_role = getattr(user, 'role', None)
        
        if user_role not in ['admin', 'moderator']:
            return HttpResponseForbidden("Access denied: Insufficient permissions.")
        
        return self.get_response(request)

