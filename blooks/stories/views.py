from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from stories.serializers import StorySerializer
from stories.models import Story
from rest_framework.renderers import JSONRenderer
def home(request):
   context = RequestContext(request,{	'request':request,
   										'user': request.user})
   return render_to_response('home.html',context_instance=context)

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into json
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


def story_list(request):
	"""
	List all stories, or create a new story
	"""
	if request.method == 'GET':
		stories = Story.objects.all()
		serializer = StorySerializer(stories, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = StorySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, 400)

def story_detail(request, pk):
	"""
	Retrive, update or delete a code snippet.
	"""
	try:
		story = Story.objects.get(pk=pk)
	except Story.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = StorySerializer(story)
		return JSONResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = StorySerializer(story, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		story.delete()
		return HttpResponse(status=204)