from django.urls import path
from .views import MetalList, MetalDetail

urlpatterns = [
  path("", MetalList.as_view(), name="metal_list"),
  path("<int:pk>/", MetalDetail.as_view(), name="metal_detail"),
]
