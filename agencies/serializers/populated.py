from .common import AgencySerializer
from users.serializers.common import UserSerializer

class PopulatedAgencySerializer(AgencySerializer):
  owner = UserSerializer()