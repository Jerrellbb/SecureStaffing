from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import User
from agencies.serializers.common import AgencySerializer
from roles.serializers.common import RoleSerializer
from shifts.serializers.common import ShiftSerializer



User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  password_confirmation = serializers.CharField(write_only=True)

  class Meta:
    model = User
    extra_fields = ['password_confirmation']
    fields = '__all__'

  def validate(self, data):
      password = data.get('password')
      password_confirmation = data.pop('password_confirmation')
      
      if password != password_confirmation:
        raise serializers.ValidationError('passwords do not match')
      return data
  
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
class UserSerializer(serializers.ModelSerializer):
  owned_agency = AgencySerializer(many=True, read_only=True)
  role = RoleSerializer()
  

  
  class Meta:
    model = User # the model that is used to serialize the queryset
    fields = ['id','owned_agency', 'username', 'email', 'role', 'accepted_shifts']# which fields to serialize