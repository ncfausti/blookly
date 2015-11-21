from rest_framework import serializers, viewsets, permissions
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
	class Meta:
		model = Story
		fields = ('id', 'title', 'author','pub_date', 'content', 'description')
		read_only_fields = ('id', 'pub_date')

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


# Make sure object user has update/delete permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user