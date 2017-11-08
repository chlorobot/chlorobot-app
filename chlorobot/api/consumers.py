from channels import Group
from channels.generic.websockets import WebsocketDemultiplexer
from api.bindings import *


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "LogValueBinding": LogValueBinding.consumer,
    }

    def connection_groups(self):
        return ["log"]

