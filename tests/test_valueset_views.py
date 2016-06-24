from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from model_mommy import mommy

from rest_framework.test import APIClient
from fhir_valuesets.valuesets.models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    SignatureType,
    AgeUnits
)


def test_api_root():
    client = APIClient()
    response = client.get('/', format='json')
    assert response.status_code == 200


class BaseViewsTest(object):

    def test_create(self):
        data = {
            'code': 'code',
            'display': 'display'
        }

        response = self.client.post(self.url_list, data, format='json')
        assert response.status_code == 201
        assert response.data['display'] == data['display']
        assert response.data['code'] == data['code']

    def test_retrieve(self):
        mommy.make(self.model, code=self.code)
        mommy.make(self.model, code=self.code2)

        response = self.client.get(self.url_list)
        assert response.data['count'] == 2
        data = [
            a['code'] for a in response.data['results']
        ]
        assert self.code in data
        assert self.code2 in data

    def test_patch(self):
        value_set = mommy.make(
            self.model,
            code='code',
            display='display'
        )
        data = {'display': 'New display'}
        url = reverse(self.url_detail, kwargs={"pk": value_set.pk})
        response = self.client.patch(url, data, format='json')

        assert response.status_code == 200
        assert response.data['display'] == data['display']

    def test_put(self):
        value_set = mommy.make(self.model)
        data = {
            'display': 'display',
            'code': 'code',
            'active': True,
        }
        url = reverse(self.url_detail, kwargs={"pk": value_set.pk})
        response = self.client.put(url, data, format='json')

        assert response.status_code == 200
        assert response.data['code'] == data['code']

    def test_delete(self):
        value_set = mommy.make(self.model)
        url = reverse(self.url_detail, kwargs={"pk": value_set.pk})
        response = self.client.delete(url, format='json')

        assert response.status_code == 204


class TestTimingAbbreviationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTimingAbbreviationViewSet, self).setUp()
        self.url_list = reverse('valuesets:timing_abbreviation-list')
        self.url_detail = 'valuesets:timing_abbreviation-detail'
        self.model = TimingAbbreviation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEventTimingViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEventTimingViewSet, self).setUp()
        self.url_list = reverse('valuesets:event_timing-list')
        self.url_detail = 'valuesets:event_timing-detail'
        self.model = EventTiming
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestUnitsOfTimeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestUnitsOfTimeViewSet, self).setUp()
        self.url_list = reverse('valuesets:units_of_time-list')
        self.url_detail = 'valuesets:units_of_time-detail'
        self.model = UnitsOfTime
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSignatureTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSignatureTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:signature_type-list')
        self.url_detail = 'valuesets:signature_type-detail'
        self.model = SignatureType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAgeUnitsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAgeUnitsViewSet, self).setUp()
        self.url_list = reverse('valuesets:age_unit-list')
        self.url_detail = 'valuesets:age_unit-detail'
        self.model = AgeUnits
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'
