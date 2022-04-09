from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('leads/', LeadsList),
    path('leads/<int:pk>/', LeadDetails),
    path('leads/create/', createLead)
]
