from . import views
from django.urls import re_path, path

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school_list'),
    re_path('(?P<pk>\d+)/', views.SchoolDetailView.as_view(), name='school_detail')
]