"""viewsets file."""
from rest_framework import viewsets

from ..models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    SignatureType,
    AgeUnits
)

from ..serializers import (
    TimingAbbreviationSerializer,
    EventTimingSerializer,
    UnitsOfTimeSerializer,
    SignatureTypeSerializer,
    AgeUnitsSerializer
)


class CommonViewSet(viewsets.ModelViewSet):
    filter_fields = ('code', 'display', 'definition')
    search_fields = ('code', 'display', 'definition')


class TimingAbbreviationViewSet(CommonViewSet):
    serializer_class = TimingAbbreviationSerializer
    queryset = TimingAbbreviation.objects.all()


class EventTimingViewSet(CommonViewSet):
    serializer_class = EventTimingSerializer
    queryset = EventTiming.objects.all()


class UnitsOfTimeViewSet(CommonViewSet):
    serializer_class = UnitsOfTimeSerializer
    queryset = UnitsOfTime.objects.all()


class SignatureTypeViewSet(CommonViewSet):
    serializer_class = SignatureTypeSerializer
    queryset = SignatureType.objects.all()


class AgeUnitsViewSet(CommonViewSet):
    serializer_class = AgeUnitsSerializer
    queryset = AgeUnits.objects.all()
