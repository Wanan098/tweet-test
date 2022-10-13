from email import message
from pyexpat import model
from rest_framework import serializers
from .models import Texts

class TextSerializer(serializers.ModelSerializer):

  user_name = serializers.CharField()
  text = serializers.CharField()
  created_at = serializers.DateTimeField(read_only=True)

  class Meta:
    model = Texts
    fields = [ 'id', 'user_name', 'text', 'created_at' ]