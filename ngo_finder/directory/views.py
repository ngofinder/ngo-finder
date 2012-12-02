from django.http import HttpResponse
from django.shortcuts import render_to_response
from directory.models import Organization

def hello_world(request):
        return render_to_response("directory/hello_world.html")

def ngo(request, ngo_id):
        organization = Organization.objects.filter(id = ngo_id)
        return render_to_response("directory/profile.html", {"organization" :organization})
