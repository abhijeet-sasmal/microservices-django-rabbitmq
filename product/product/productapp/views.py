from rest_framework import permissions, viewsets
from .models import Products
from .serializers import ProductSerializer

class Products(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated()]