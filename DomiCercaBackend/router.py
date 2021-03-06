from rest_framework import routers, serializers, viewsets
from apps.user.views import UserViewSet
from apps.domicilio.views import DomicilioViewset

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'domicilio', DomicilioViewset)