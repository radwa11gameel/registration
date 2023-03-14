from .models import Product
from .serializers import ProductSeliarizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics


class ProductApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSeliarizer
    queryset = Product.objects.all()
    # lookup_fields = 'id'
