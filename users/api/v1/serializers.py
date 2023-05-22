from rest_framework import serializers
from users.models import Just_one_field,Model3,Model4,Model5,Model6

class Model4Serializer(serializers.ModelSerializer):

    class Meta:
        model = Model4
        fields = "__all__"

class Just_one_fieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Just_one_field
        fields = "__all__"

class Model5Serializer(serializers.ModelSerializer):

    class Meta:
        model = Model5
        fields = "__all__"

class Model3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Model3
        fields = "__all__"

class Model6Serializer(serializers.ModelSerializer):

    class Meta:
        model = Model6
        fields = "__all__"