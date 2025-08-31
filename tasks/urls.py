from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet

# Using DRF's DefaultRouter to automatically create CRUD routes
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', CategoryViewSet, basename='category')

# Export router URLs
urlpatterns = router.urls

