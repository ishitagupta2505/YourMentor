import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class TeacherFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='iexact')
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['profile_pic', 'Password']