from rest_framework.generics import RetrieveUpdateDestroyAPIView
from lib.views import OwnerListCreateView
from .models import Security
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers.common import SecuritySerializer
from .serializers.populated import PopulatedSecuritySerializer

# Create your views here.
class SecurityListCreateView(OwnerListCreateView):
  queryset = Security.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedSecuritySerializer
    return SecuritySerializer
  
class SecurityDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Security.objects.all()

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedSecuritySerializer
    else:
      return SecuritySerializer