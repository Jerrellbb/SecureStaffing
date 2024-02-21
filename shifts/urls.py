from django.urls import path
from .views import ShiftAcceptView, ShiftListCreateVIew, ShiftDetailView, ShiftRejectView

urlpatterns = [
    path('', ShiftListCreateVIew.as_view()),
    path('<int:pk>/', ShiftDetailView.as_view()),
    path('<int:shift_id>/accept', ShiftAcceptView.as_view()),
    path('<int:shift_id>/reject', ShiftRejectView.as_view())
]