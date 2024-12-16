from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Material
from .serializers import MaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_name = request.query_params.get('category', None)
        if category_name:
            materials = Material.objects.filter(category__iexact=category_name)
            serializer = self.get_serializer(materials, many=True)
            return Response(serializer.data)
        return Response({"message": "Category parameter is required."}, status=status.HTTP_400_BAD_REQUEST)


class UniqueCategoriesView(APIView):
    def get(self, request):
        categories = Material.objects.values_list('category', flat=True).distinct()
        return Response({"categories": list(categories)}, status=status.HTTP_200_OK)


class SubCategoryView(APIView):
    def get(self, request, category_name=None):
        if category_name:
            materials = Material.objects.filter(category__iexact=category_name)
            if not materials.exists():
                return Response({"message": "No materials found for this category."}, status=status.HTTP_404_NOT_FOUND)
            serializer = MaterialSerializer(materials, many=True)
            return Response({"materials": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Category name is required."}, status=status.HTTP_400_BAD_REQUEST)


class MaterialDetailView(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer