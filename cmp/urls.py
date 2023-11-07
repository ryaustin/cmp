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

    # Country URLs
    path('countries/', views.countries, name='countries'),
    path("mgmt/countries", views.edit_countries, name="countries"),
    path("mgmt/countries/<int:country_id>/", views.detail_countries, name="countries"),
    path("mgmt/countries/edit/<int:country_id>", views.edit_countries, name="edit-countries"),

    path('ranks/', views.ranks, name='ranks'),
    path("mgmt/ranks", views.edit_ranks, name="ranks"),

    path('cemeteries/', views.cemeteries, name='cemeteries'),
    path("mgmt/cemeteries", views.edit_cemeteries, name="cemeteries"),

    path('pow-camps/', views.powcamps, name='powcamps'),
    path("mgmt/pow-camps", views.edit_powcamps, name="powcamps"),

]
