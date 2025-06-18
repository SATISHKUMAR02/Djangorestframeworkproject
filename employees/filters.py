import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    branch = django_filters.CharFilter(field_name='e_branch',lookup_expr='iexact')
    e_name = django_filters.CharFilter(field_name='e_name',lookup_expr='icontains')
    id =django_filters.RangeFilter(field_name='id')
    class Meta:
        model = Employee
        fields = ['e_branch','e_name','id']
        