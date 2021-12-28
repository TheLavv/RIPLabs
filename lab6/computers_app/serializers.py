from computers_app.models import Computer
from rest_framework import serializers


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Computer
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "cost", "description", "date_modified"]
