from django.urls import path

from .views import gptfunc

urlpatterns = [



    path('gpt/', gptfunc, name="gptfunc"),
    

    
]