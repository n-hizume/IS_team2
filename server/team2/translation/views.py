from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import translate

def gptfunc(request):
    if request.method == 'POST':
        
        json_str = request.body
        response = translate.translate(json_str)
        return HttpResponse(response)
        """try:
            user = User.objects.
        except IntegrityError:
            return render(request, '.html', {'error':''})"""
    else: 
        return HttpResponse('POST ONLY')