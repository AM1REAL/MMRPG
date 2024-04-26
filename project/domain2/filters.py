from django_filters import FilterSet
from .models import *

class ResponsesFilter(FilterSet):
    class Meta:
        model = Response
        fields = {
            'response_text': ['icontains']
        }
