from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        query_set = Task.objects.all()
        request: Request = self.request # Ignore IDE TypeError
        status = request.query_params.get("status")

        # Filter on Status Directly
        if status:
            if status not in Task.Status.values:
                raise ValidationError("Invalid Query Param Status")
            query_set = query_set.filter(status=status)
        return query_set