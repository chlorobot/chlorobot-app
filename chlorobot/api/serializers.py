from rest_framework import serializers
from api.models import *
from django_db_logger.models import StatusLog


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusLog
        fields = ('__all__')

