from rest_framework import serializers
from .models import Metal

class MetalSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "owner", "name", "description", "symbol", "created_at")
    model = Metal
