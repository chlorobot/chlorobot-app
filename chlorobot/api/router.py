from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'logs', views.LogViewSet)

