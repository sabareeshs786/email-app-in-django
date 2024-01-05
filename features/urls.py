from django.urls import path
from features import views

urlpatterns = [
    path('inbox', views.inbox, name="inbox"),
    
]