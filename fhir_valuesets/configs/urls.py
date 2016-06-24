from django.conf.urls import include, url
from fhir_valuesets.valuesets import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^valuesets/', include('fhir_valuesets.valuesets.urls',
        namespace='valuesets'))
]
