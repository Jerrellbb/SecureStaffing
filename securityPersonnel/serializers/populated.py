from .common import SecuritySerializer
from users.serializers.common import UserSerializer

class PopulatedSecuritySerializer(SecuritySerializer):
  user = UserSerializer()