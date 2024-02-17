from rest_framework import ModelSerializers
from ..models import Agency

class AgencySerializer(ModelSerializers):
  
  class Meta:
    model = Agency 
    fields = '__all__'