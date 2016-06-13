from django.test import TestCase
from rest_framework import generics
from rest_framework.test import APIRequestFactory

from fhir_valuesets.valuesets.search import CommonSearchFilter
from fhir_valuesets.valuesets.models import AgeUnits
from fhir_valuesets.valuesets.serializers import AgeUnitsSerializer


factory = APIRequestFactory()


class TestSearchFilter(TestCase):
    def setUp(self):
        # Sequence of display/code is:
        #
        # z   abc
        # zz  bcd
        # zzz cde
        # ...
        for idx in range(10):
            code = 'z' * (idx + 1)
            display = (
                chr(idx + ord('a')) +
                chr(idx + ord('b')) +
                chr(idx + ord('c'))
            )
            AgeUnits(code=code, display=display).save()

    def test_search(self):
        class SearchView(generics.ListCreateAPIView):
            queryset = AgeUnits.objects.all()
            serializer_class = AgeUnitsSerializer
            filter_backends = (CommonSearchFilter,)
            search_fields = ('code', 'display')

        view = SearchView.as_view()
        request = factory.get('/', data={'search': 'bc'})
        response = view(request)
        self.assertEqual(response.data.get('count'), 1)

    def test_search_exact(self):
        class SearchView(generics.ListCreateAPIView):
            queryset = AgeUnits.objects.all()
            serializer_class = AgeUnitsSerializer
            filter_backends = (CommonSearchFilter,)
            search_fields = ('=code', '=display')

        view = SearchView.as_view()
        request = factory.get('/', data={'search': 'abc'})
        response = view(request)
        self.assertEqual(response.data.get('count'), 1)

    def test_search_starts_with(self):
        class SearchView(generics.ListCreateAPIView):
            queryset = AgeUnits.objects.all()
            serializer_class = AgeUnitsSerializer
            filter_backends = (CommonSearchFilter,)
            search_fields = ('^code', '$display')

        view = SearchView.as_view()
        request = factory.get('/', data={'search': 'b'})
        response = view(request)
        self.assertEqual(response.data.get('count'), 2)

    def test_search_icontains(self):
        class SearchView(generics.ListCreateAPIView):
            queryset = AgeUnits.objects.all()
            serializer_class = AgeUnitsSerializer
            filter_backends = (CommonSearchFilter,)
            search_fields = ('~code', '~display')

        view = SearchView.as_view()
        request = factory.get('/', data={'search': 'bc'})
        response = view(request)
        self.assertEqual(response.data.get('count'), 2)
