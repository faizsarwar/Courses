import django_filters
from django_filters import DateFilter
from .models import *

class todofilter(django_filters.FilterSet):     #isko view mai import krwana parayga 
    class Meta:
        model = tasks
        fields='__all__'
        exclude=['profile','created']