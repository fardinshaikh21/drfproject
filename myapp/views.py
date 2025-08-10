# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})