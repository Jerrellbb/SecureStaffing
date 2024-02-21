from rest_framework.generics import RetrieveUpdateDestroyAPIView
from lib.views import  OwnerListCreateView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Shift
from .serializers.populated import PopulatedShiftSerialzer
from .serializers.common import ShiftSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ShiftListCreateVIew(OwnerListCreateView):
  queryset = Shift.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedShiftSerialzer
    return ShiftSerializer
  
class ShiftDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Shift.objects.all()

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return PopulatedShiftSerialzer
    else:
      return ShiftSerializer
    

class ShiftAcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, shift_id):
        try:
            shift = Shift.objects.get(pk=shift_id)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found'}, status=status.HTTP_404_NOT_FOUND)

        if shift.available_slots <= 0:
            return Response({'error': 'No available slots for this shift'}, status=status.HTTP_400_BAD_REQUEST)

        if request.user in shift.accepted_users.all():
            return Response({'error': 'You have already accepted this shift'}, status=status.HTTP_400_BAD_REQUEST)

        shift.accepted_users.add(request.user)
        shift.available_slots -= 1
        shift.save()
        return Response({'message': 'Shift has been accepted'}, status=status.HTTP_200_OK)

class ShiftRejectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, shift_id):
        try:
            shift = Shift.objects.get(pk=shift_id)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.user in shift.accepted_users.all():
            shift.accepted_users.remove(request.user)
            shift.available_slots += 1
            shift.save()
            return Response({'message': 'Shift has been rejected'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You have not accepted this shift'}, status=status.HTTP_400_BAD_REQUEST)