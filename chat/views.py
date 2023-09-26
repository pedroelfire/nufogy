from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *

# Create your views here.

class ChatView(APIView):
    serializer_class = chatSerializer

    def get(self, request):
        detail = [{"title": detail.title, "text": detail.text}
        for detail in message.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = chatSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

