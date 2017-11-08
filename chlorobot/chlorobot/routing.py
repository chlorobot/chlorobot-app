from channels.routing import route, route_class
from api.consumers import Demultiplexer

channel_routing = [
    route_class(Demultiplexer, path="^/ws/"),
]


