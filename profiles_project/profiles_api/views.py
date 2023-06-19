from ast import Return
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers




class HelloApiView(APIView):

    serializer_class=serializers.helloSerializer

    def get(self,request,format=None):

        """Retornar lista de caracteristicas del APIView"""

        an_apiview = [
            'Usamos metoos HTTP como funciones (get,post,patch,put,delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra app',
            'Está mapeado manualmente a los URLs',

        ]

        dict_ret={'message':'Hello','an_apiview':an_apiview}

        return Response(dict_ret) 
    

    def post(self,request):

        """Crea  un mensaje con nuestro nombre"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hello {name}'
            dict_ret={'message':message}

            return Response(dict_ret)
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST 
            )
    
    def put(self,request,pk=None):
        """Maneja Actualizar un objeto"""
        return Response({'method':'PUT'})

    def patch (self, request, pk=None):

        """Maneja actualizacion parcial de un objeto"""

        return Response({'method': 'PATCH'})

    
    def delete (self,request,pk=None):
        """Borrar un objeto"""
        """Borrar otro archivo lol"""
        print ("")

        return Response ({'method': "DELETE"})

