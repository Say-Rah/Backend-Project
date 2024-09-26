from django.urls import path
from .views import StudySessionListCreateView, StudySessionDetailView

urlpatterns = [
    path('session/', StudySessionListCreateView.as_view(), name='session-list-create'),
    path('session/<int:pk>/', StudySessionDetailView.as_view(), name='session-detail'),
]
