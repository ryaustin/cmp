from django.urls import path, include
#from .views import index
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("sentry-debug/", views.trigger_error ),
    path("tools/army-number-search", views.army_number_search, name="army-number-search" ),
    path("tools/army-number-search/<int:army_number>"  , views.original_unit, name="army-number-search" ),
]
