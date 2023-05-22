from rest_framework import authentication
from users.models import Just_one_field,Model3,Model4,Model5,Model6
from .serializers import Just_one_fieldSerializer,Model3Serializer,Model4Serializer,Model5Serializer,Model6Serializer
from rest_framework import viewsets

class Model4ViewSet(viewsets.ModelViewSet):
    serializer_class = Model4Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Model4.objects.all()

class Just_one_fieldViewSet(viewsets.ModelViewSet):
    serializer_class = Just_one_fieldSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Just_one_field.objects.all()

class Model5ViewSet(viewsets.ModelViewSet):
    serializer_class = Model5Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Model5.objects.all()

class Model3ViewSet(viewsets.ModelViewSet):
    serializer_class = Model3Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Model3.objects.all()

class Model6ViewSet(viewsets.ModelViewSet):
    serializer_class = Model6Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Model6.objects.all()