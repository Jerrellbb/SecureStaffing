from django.urls import path
from .views import AgencyListCreateView, AgencyDetailView
urlpatterns = [
    path('', AgencyListCreateView.as_view()),
    path('<int:pk>/', AgencyDetailView.as_view())
    

]