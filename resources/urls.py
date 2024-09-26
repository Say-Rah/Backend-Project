from django.urls import path
from .views import ResourceListCreateView, ResourceDetailView

urlpatterns = [
    path('/resource/', ResourceListCreateView.as_view(), name='resource-list-create'),
    path('/resource/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
]
