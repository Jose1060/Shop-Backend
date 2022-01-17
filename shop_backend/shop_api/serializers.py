from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serealizer un campo para probar """
    name = serializers.CharField(max_length=10)