from django.urls import path, re_path
from .views import dummy_view

urlspatterns = [
    path('', dummy_view, name='entry-list'),
    path('<int:id>/'. dummy_view, name='entry-detail'),
    path('<str:name>/'. dummy_view, name='entry-detail'),
    path('<uuid:name>/'. dummy_view, name='entry-detail'),
    path('<slug:name>/'. dummy_view, name='entry-detail'),
    path('(?P<id>[0-9]{4})/$'. dummy_view, name='entry-detail'),
    path('<id>/delete/', dummy_view, name='entry-delete'),
    path('<id>/update/', dummy_view, name='entry-update')
]