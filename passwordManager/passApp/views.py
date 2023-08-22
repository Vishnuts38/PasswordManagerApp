from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,PasswordSerializer,PasswordShareSerializer, OrganisationSerializer  
from .models import PasswordItem,PasswordShare, Organisation

class UserSignupView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class passwordCreate(generics.ListCreateAPIView):
    queryset = PasswordItem.objects.all()
    serializer_class = PasswordSerializer  


class rudPassword(generics.RetrieveUpdateDestroyAPIView):  
    # authentication_classes = []

    serializer_class = PasswordSerializer
    queryset = PasswordItem.objects.all()

class passwordShareCreate(generics.ListCreateAPIView):
    queryset = PasswordShare.objects.all()
    serializer_class = PasswordShareSerializer 

class organisationCreate(generics.ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer 