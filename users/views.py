from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers.common import RegistrationSerializer, UserSerializer
from .serializers.populated import PopulatedUserSerializer
from django.contrib.auth import get_user_model
from lib.permissions import IsOwnerOrReadOnly
User = get_user_model()
# Create your views here.

class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegistrationSerializer

class UserView(ListAPIView):
  queryset = User.objects.all()
  serializer_class = PopulatedUserSerializer

class UserSingleView(RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = PopulatedUserSerializer
  permission_classes = [IsOwnerOrReadOnly]
  

  def get_serializer_class(self):

    if self.request.method == 'PUT':
      return UserSerializer
    return PopulatedUserSerializer