from django.http import HttpResponse
from django.shortcuts import render_to_response
from directory.models import Organization, Comment
from django.core.context_processors import csrf
from django.template import RequestContext

def hello_world(request):
    c = RequestContext(request,{})
    c.update(csrf(request))
    return render_to_response("directory/hello_world.html",c)

def ngo(request, ngo_id):
    organization = Organization.objects.filter(id = ngo_id).get()    
    if request.POST:
        comment_text = request.POST.get('comment')
        comment = Comment()
        comment.organization = organization
        comment.user = request.user
        comment.subject = request.POST.get('subject')
        comment.text = comment_text
        comment.save()
    c = RequestContext(request,{"organization" : organization})
    c.update(csrf(request))
    return render_to_response("directory/profile.html", c)
    
