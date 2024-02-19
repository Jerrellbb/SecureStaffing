from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from .models import Agency
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers.common import AgencySerializer
from .serializers.populated import PopulatedAgencySerializer
from lib.views import OwnerListCreateView
# Create your views here.

class AgencyListCreateView(OwnerListCreateView):
  queryset = Agency.objects.all()
  
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedAgencySerializer
    return AgencySerializer
  
class AgencyDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Agency.objects.all()

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedAgencySerializer
    else:

      return AgencySerializer