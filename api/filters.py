import django_filters
from .models import Course_post


class Course_postFilter(django_filters.FilterSet):
    class Meta:
        model = Course_post
        fields = {
            'subject': ['icontains'],
            'name': ['icontains'],
            'UserType': ['exact'],
            'date': ['lt', 'gt'],
            'postType': ['exact']
        }
