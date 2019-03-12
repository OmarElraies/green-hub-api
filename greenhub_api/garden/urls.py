from django.urls import path, include
from rest_framework.routers import DefaultRouter
from garden import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'garden', views.PlantsViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]