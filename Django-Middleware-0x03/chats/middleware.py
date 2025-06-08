# chats/middleware.py

from datetime import datetime, time
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
