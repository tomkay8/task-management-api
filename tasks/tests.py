from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.utils import timezone
from .models import Task, Category


class TaskAPITestCase(APITestCase):
    """
    Automated tests for Task API.
    Covers: authentication, creation, listing, filtering, updating, deleting.
    """

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        # Create a category
        self.category = Category.objects.create(name="Work")

        # Create a sample task
        self.task = Task.objects.create(
            title="Sample Task",
            description="This is a test task",
            status="pending",
            category=self.category,
            user=self.user,
            due_date=timezone.now() + timezone.timedelta(days=7)
        )

    def test_create_task(self):
        """
        Ensure a task can be created successfully.
        """
        url = reverse("task-list")
        data = {
            "title": "New Task",
            "description": "Automated test task",
            "status": "pending",
            "category": self.category.id,
            "due_date": (timezone.now() + timezone.timedelta(days=5)).isoformat()
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_list_tasks(self):
        """
        Ensure tasks are listed correctly.
        """
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_tasks_by_status(self):
        """
        Ensure filtering tasks by status works.
        """
        url = reverse("task-list") + "?status=pending"  # ✅ corrected
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for task in response.data:
            self.assertEqual(task["status"], "pending")

    def test_update_task(self):
        """
        Ensure a task can be updated.
        """
        url = reverse("task-detail", args=[self.task.id])
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "status": "done",
            "category": self.category.id,
            "due_date": (timezone.now() + timezone.timedelta(days=10)).isoformat()
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "done")

    def test_delete_task(self):
        """
        Ensure a task can be deleted.
        """
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

