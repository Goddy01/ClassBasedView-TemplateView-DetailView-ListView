from . import views
from django.urls import re_path, path

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school_list'),
    re_path('^(?P<pk>\d+)/', views.SchoolDetailView.as_view(), name='school_detail'),
    re_path('^create_school/$', views.SchoolCreateView.as_view(), name='create_school'),
    re_path('^update_school/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update_school'),
]