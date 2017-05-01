from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def call(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'call.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def handler404(request):
    return render(request, '404.html')
    #response = render_to_response('404.html', {},
    #                          context_instance=RequestContext(request))
    #response.status_code = 404
    #return response


def handler500(request):
    return render(request, '500.html')
    #response = render_to_response('500.html', {},
    #                          context_instance=RequestContext(request))
    #response.status_code = 500
    #return response