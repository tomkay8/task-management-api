from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Task model
class TaskViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for Tasks:
    - GET: List or retrieve tasks
    - POST: Create a new task
    - PUT/PATCH: Update an existing task
    - DELETE: Delete a task
    Only authenticated users can access tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the task owner when creating a task.
        """
        serializer.save(user=self.request.user)

# ViewSet for Category model
class CategoryViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for Task Categories:
    - GET: List or retrieve categories
    - POST: Create a new category
    - PUT/PATCH: Update a category
    - DELETE: Delete a category
    Only authenticated users can access categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

