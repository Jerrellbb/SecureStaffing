from django.urls import path
from .views import SecurityListCreateView, SecurityDetailView
urlpatterns = [
    path('', SecurityListCreateView.as_view()),
    path('<int:pk>/', SecurityDetailView.as_view())
]