from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

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
                raise ValidationError({
                    "status": f"Invalid status '{status}'. Must be one of {list(Task.Status.values)}"
                })

            query_set = query_set.filter(status=status)
        return query_set

    # Fetches all tasks that have been archived
    # Fetching non archived tasks can be done by filtering on "Active" status
    # /archived
    @action(detail=False, methods=["get"])
    def get_archived(self, request):
        archived_tasks = Task.objects.filter(
            status__in=[Task.Status.EXPIRED, Task.Status.COMPLETE]
        )
        serializer = self.get_serializer(archived_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Marks a given task as complete
    # /{id}/complete
    @action(detail=True, methods=["put"], url_path="complete")
    def mark_as_complete(self, request):
        task = self.get_object()
        task.status = Task.Status.COMPLETE
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)