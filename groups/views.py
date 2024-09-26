from rest_framework import viewsets
from .models import StudyGroup
from .serializers import StudyGroupSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)