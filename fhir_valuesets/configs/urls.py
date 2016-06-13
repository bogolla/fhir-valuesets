from django.conf.urls import include, url


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^valuesets/', include('fhir_valuesets.valuesets.urls',
        namespace='valuesets'))

    # url(r'^search/$', GlobalSearchList.as_view(), name="search")
]
