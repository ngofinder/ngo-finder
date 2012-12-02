from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    signed_in = False
    if request.POST:
        if request.POST.get('signed_in'):
            c = RequestContext(request,{})
            c.update(csrf(request))
            return redirect('/',c)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                state = "You're successfully logged in"
                signed_in = True
            else:
                state = "Your account is not active, please contact the site admin"
                signed_in = False
        else:
            state = "Your username and/or password were incorrect"
            signed_in = False

    c = RequestContext(request, { 
                                    'state'    : state,
                                    'username' : username,
                                    'signed_in': signed_in})
    c.update(csrf(request))

    return render_to_response('auth/signin.html',c)

