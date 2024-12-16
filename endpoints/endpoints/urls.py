from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from material import views  

# Define a router for MaterialViewSet
router = routers.DefaultRouter()
router.register(r'materials', views.MaterialViewSet, basename='materials')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/categories/', views.UniqueCategoriesView.as_view(), name='unique-categories'),

    path('api/categories/<str:category_name>/', views.SubCategoryView.as_view(), name='category-materials'),
    path('api/material/<int:pk>/', views.MaterialDetailView.as_view(), name='material-detail'),

]
