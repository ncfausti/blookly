from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from stories.models import Story
from django.contrib import admin


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StorySerializer(serializers.ModelSerializer):
	author = UserSerializer(read_only=True, required=False)

	class Meta:
		model = Story
		fields = ('id', 'title', 'author','pub_date', 'content', 'description')
		read_only_fields = ('id', 'pub_date')

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer