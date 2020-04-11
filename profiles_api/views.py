from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
           'Uses HTTP methods as function (get, post patch, put, delete)',
           'Is similar to a traditional Django View',
           'Gives you the most control over your application logic',
           'Is mapped manually to URLs',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'










