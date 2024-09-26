from rest_framework import generics
from .models import StudySession
from .serializers import StudySessionSerializer

# Create and List Sessions
class StudySessionListCreateView(generics.ListCreateAPIView):
    queryset = StudySession.objects.all()
    serializer_class = StudySessionSerializer

# Retrieve, Update, and Delete a Session
class StudySessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudySession.objects.all()
    serializer_class = StudySessionSerializer
