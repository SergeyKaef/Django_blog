from django.urls import path
from .views import BlogListView, debug_view


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('debug/', debug_view, name='debug'),
]