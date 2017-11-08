from rest_framework import viewsets
from api.serializers import *
from api.models import *
from django.shortcuts import render
from django_db_logger.models import StatusLog
import logging

logger = logging.getLogger('db')


def index(request) :
    return render(request, 'index.html')


class LogViewSet(viewsets.ModelViewSet):
    queryset = StatusLog.objects.all()
    serializer_class = LogSerializer


