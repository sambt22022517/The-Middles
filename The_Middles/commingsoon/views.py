from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def test_commingsoon(request):
    template = loader.get_template('commingsoon/comming-soon.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))