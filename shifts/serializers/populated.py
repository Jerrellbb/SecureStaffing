from .common import ShiftSerializer
from agencies.serializers.common import AgencySerializer
from rest_framework import serializers

class PopulatedShiftSerialzer(ShiftSerializer):
  agency_name = serializers.SerializerMethodField()

  def get_agency_name(self, obj):
        return obj.agency.name 
