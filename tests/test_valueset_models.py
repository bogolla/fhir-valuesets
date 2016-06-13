from django.test import TestCase
from model_mommy import mommy

from fhir_valuesets.valuesets.models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    SignatureType,
    AgeUnits
)


class TestTimingAbbreviation(TestCase):
    def test_unicode(self):
        display = "Q4H"
        data = mommy.make(TimingAbbreviation, display=display)
        assert str(data) == display


class TestEventTiming(TestCase):
    def test_unicode(self):
        display = "EventTiming"
        data = mommy.make(EventTiming, display=display)
        assert str(data) == display


class TestUnitsOfTime(TestCase):
    def test_unicode(self):
        display = "UnitsOfTime"
        data = mommy.make(UnitsOfTime, display=display)
        assert str(data) == display


class TestSignatureType(TestCase):
    def test_unicode(self):
        display = "SignatureType"
        data = mommy.make(SignatureType, display=display)
        assert str(data) == display


class TestAgeUnits(TestCase):
    def test_unicode(self):
        display = "AgeUnits"
        data = mommy.make(AgeUnits, display=display)
        assert str(data) == display
