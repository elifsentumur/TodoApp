from rest_framework import status
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from app.models import ProviderModel,DeveloperModel,TaskModel
from app.api.serializers import ProviderSerializer,DeveloperSerializer,TaskSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView


class ProviderList(ListAPIView):
    queryset= ProviderModel.objects.all()
    serializer_class = ProviderSerializer

class DeveloperList(ListAPIView):
    queryset = DeveloperModel.objects.all()
    serializer_class = DeveloperSerializer

class DeveloperDetail(RetrieveAPIView):
    queryset = DeveloperModel.objects.all()
    serializer_class = DeveloperSerializer
    lookup_field= 'slug'
    

class ProviderDetail(RetrieveAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderSerializer
    # lookup_field= 'slug'

class TaskList(ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

