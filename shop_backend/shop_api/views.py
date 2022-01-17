from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shop_api import serializers

class HelloWorld(APIView):
    ''' Api View Prueba '''
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        ''' Devuelve un saludo '''
        an_apiview = [
        'Usamos metodos http para crear una app rest como funciones (get, post, put, patch, delete)',
        "Es similar a una vista tradicinal de Django",
        "Nos da el mayor control sobre la logica de nuestra aplicacion",
        "Esta mapeado manualmente a los URLs"
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})

    def post(self, request):
        ''' Crea un nuevo saludo con un nombre dado '''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk= None):
        """Maneja actualizar un objeto"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk= None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk= None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
