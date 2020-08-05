import django_filters
from .models import Job


class ProductFilter(django_filters.FilterSet):
    # price__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner', 'slug', 'image', 'publish_at', 'salary',)