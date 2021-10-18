from rest_framework import serializers
from app.models import ProviderModel,DeveloperModel,TaskModel

class ProviderSerializer(serializers.Serializer):
    name = serializers.CharField()
    endpoint = serializers.CharField()

    def create(self,validated_data):
        return ProviderModel.objects.create(**validated_data)

    def update(self, instance,validated_data):
        instance.name =  validated_data.get('name',instance.name)
        instance.endpoint = validated_data.get('endpoint',instance.endpoint)

class DeveloperSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = DeveloperModel
        fields = ['id', 'name', 'task','level','duration','slug',]
 
class TaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = TaskModel
        fields = ['id', 'provider','name', 'level','duration',]
 