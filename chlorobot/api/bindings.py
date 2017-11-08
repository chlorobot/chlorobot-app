from channels.binding.websockets import WebsocketBinding
from api.models import *
from django_db_logger.models import StatusLog


class LogValueBinding(WebsocketBinding):

    model = StatusLog
    stream = "log"
    fields = ["__all__"]

    @classmethod
    def group_names(cls, instance):
        return ["log"]

    def has_permission(self, user, action, pk):
        return True

