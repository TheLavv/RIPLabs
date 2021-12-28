from rest_framework import viewsets
from computers_app.serializers import ComputerSerializer
from computers_app.models import Computer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all().order_by('date_modified')
    serializer_class = ComputerSerializer  # Сериализатор для модели
