from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from stories.serializers import UserViewSet, StoryViewSet
from stories import views
from stories.models import Story

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stories', StoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^stories/$', views.story_list),
    url(r'^stories/(?P<pk>[0-9]+)/$', views.story_detail),
	url(r'^api/', include(router.urls)),
   	url(r'^$', 'stories.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]