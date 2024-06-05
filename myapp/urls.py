# core/urls.py
from django.urls import path,include
from . import views
from .api_views import QueryCountView

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('query-count/', QueryCountView.as_view(), name='query-count'),
    path('query/', views.query_builder, name='query_builder'),
    path('users/', views.user_list, name='user_list'),
]
