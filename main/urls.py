from django.urls import path
from.views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('contact/', ContactView, name='contact_url'),
    path('booknow/', BooknowView, name='booknow_url'),
    path('room/', RoomsView, name='booknow_url'),
    path('blog/', BlogView, name='blog_url'),
    path('about/', AboutView, name='about_url'),
    path('staff/', StaffView, name='staff_url'),
    path('contact2/', Contact2View, name='contact2_url'),
]