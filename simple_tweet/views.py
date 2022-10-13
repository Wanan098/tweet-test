from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from simple_tweet.models import Texts
from simple_tweet.serializers import TextSerializer

# Create your views here.
class TextView(TemplateView):
  template_name = "index.html"


class TextApiView(APIView):

  def get(self, request):
    texts = Texts.objects.values()
    return Response({ "texts": texts }, status=status.HTTP_200_OK)
  
  def post(self, request):
    data = request.data
    serializer = TextSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({ "newText": serializer.data}, status=status.HTTP_201_CREATED)