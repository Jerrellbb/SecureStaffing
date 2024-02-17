from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Agency
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers.common import AgencySerializer
# Create your views here.

class AgencyCreateView(ListCreateAPIView):
  queryset = Agency.objects.all()
  serializer_class = AgencySerializer
  permission_classes = [IsAuthenticatedOrReadOnly]