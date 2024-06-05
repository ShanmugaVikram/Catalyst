# core/api_urls.py
from django.urls import path
from .api_views import QueryCountView

urlpatterns = [
    path('query-count/', QueryCountView.as_view(), name='query-count'),
]
