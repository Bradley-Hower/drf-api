from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Metal
from .serializers import MetalSerializer

class MetalList(ListCreateAPIView):
  queryset = Metal.objects.all()
  serializer_class = MetalSerializer

class MetalDetail(RetrieveUpdateDestroyAPIView):
  queryset = Metal.objects.all()
  serializer_class = MetalSerializer
