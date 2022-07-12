from django.urls import path
from .views import *
urlpatterns = [
    path('', index_view, name='dashboard_url'),
    path('workers/', workers, name='workers_url'),
    path('worker/create/', worker_create, name='worker_create_url'),
    path('requests/', requests, name='requests_url'),
]