from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]