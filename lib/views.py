from rest_framework.generics import ListCreateAPIView

class OwnerListCreateView(ListCreateAPIView):

    def perform_create(self, serializer):
      print('REQUEST USER ->', self.request.user)
      serializer.save(owner=self.request.user)


# class AgencyJobListCreateView(ListCreateAPIView):

#     def perform_create(self, serializer):
#       agency = self.request.user.agency
#         # Set the agency field of the shift to the associated agency
#       serializer.save(agency=agency)
      
