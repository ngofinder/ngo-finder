from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext

def hello_world(request):
    c = RequestContext(request,{})
    c.update(csrf(request))
    return render_to_response("directory/hello_world.html",c)
