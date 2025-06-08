import django_filters
from .models import Message
from django.utils.timezone import make_aware
from datetime import datetime

class MessageFilter(django_filters.FilterSet):
    start_date = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='lte')
    user = django_filters.CharFilter(field_name='sender__user_id', lookup_expr='exact')

    class Meta:
        model = Message
        fields = ['user', 'start_date', 'end_date']
