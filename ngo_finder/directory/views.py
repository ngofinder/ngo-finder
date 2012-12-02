from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello_world(request):
	return render_to_response("directory/hello_world.html")
