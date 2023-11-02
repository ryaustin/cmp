from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from .views import index
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("sentry-debug/", views.trigger_error ),
    path("tools/army-number-search", views.army_number_search, name="army-number-search" ),
    path("tools/army-number-search/<int:army_number>"  , views.original_unit, name="army-number-search" ),
    path('countries/', views.countries, name='countries'),
    path('ranks/', views.ranks, name='ranks'),
    path("mgmt/countries", views.edit_countries, name="countries"),
    path("mgmt/ranks", views.edit_ranks, name="ranks"),
]
