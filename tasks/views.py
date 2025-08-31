from rest_framework import generics, viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

# --- ViewSets (used for DRF routers) ---
class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for tasks via router-based endpoints.
    Example: /api/tasks/
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Ensure the logged-in user is set as the owner of the task.
        """
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for categories via router-based endpoints.
    Example: /api/categories/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# --- Generic Views (used for extra flexibility like filtering) ---
class TaskListView(generics.ListCreateAPIView):
    """
    Custom task list view with optional filtering by status.
    Example: /api/tasks/?status=pending
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Override get_queryset to allow filtering tasks by status.
        Example: /api/tasks/?status=pending
        """
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
