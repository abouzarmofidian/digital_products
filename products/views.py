from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category,File,Product
from .serializers import CategorySerializer,FIleSerializer,ProductSerializer


# Create your views here.

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)

