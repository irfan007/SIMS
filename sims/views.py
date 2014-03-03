from django.shortcuts import render_to_response
from django.template.context import RequestContext



def index(request):
    ci = RequestContext(request)
    return render_to_response('index.html', ci)


