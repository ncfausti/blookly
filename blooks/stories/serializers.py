from rest_framework import serializers
from django.contrib.auth.models import User
from stories.models import Story
from blooks.urls import UserSerializer

class StorySerializer(serializers.ModelSerializer):
	author = UserSerializer(read_only=True, required=False)

	class Meta:
		model = Story
		fields = ('id', 'title', 'author','pub_date', 'content', 'desription')
		read_only_fields = ('id', 'pub_date')