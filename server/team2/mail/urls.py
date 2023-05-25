"""from django.urls import path
from .views import InitialView

urlpatterns = [
    path('',  ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]"""

from django.urls import path

from .views import getmailfunc, sendmailfunc, gettokenfunc

urlpatterns = [

    path('getall/', getmailfunc, name="getmailfunc"),
    path('send/', sendmailfunc, name="sendmailfunc"),
    path('auth/', gettokenfunc, name='gettokenfunc')
    
]