"""viewsets file."""
from rest_framework import viewsets

from .models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    IdentifierUse,
    IdentifierType,
    ContactPointSystem,
    ContactPointUse,
    AddressUse,
    AddressType,
    SignatureType,
    NameUse,
    QuantityComparator,
    AgeUnits,
    NarrativeStatus
)

from .serializers import (
    TimingAbbreviationSerializer,
    EventTimingSerializer,
    UnitsOfTimeSerializer,
    IdentifierUseSerializer,
    IdentifierTypeSerializer,
    ContactPointSystemSerializer,
    ContactPointUseSerializer,
    AddressUseSerializer,
    AddressTypeSerializer,
    SignatureTypeSerializer,
    NameUseSerializer,
    QuantityComparatorSerializer,
    AgeUnitsSerializer,
    NarrativeStatusSerializer

)


class TimingAbbreviationViewSet(viewsets.ModelViewSet):
    serializer_class = TimingAbbreviationSerializer
    queryset = TimingAbbreviation.objects.all()
    filter_fields = TimingAbbreviation._meta.get_all_field_names()


class EventTimingViewSet(viewsets.ModelViewSet):
    serializer_class = EventTimingSerializer
    queryset = EventTiming.objects.all()
    filter_fields = EventTiming._meta.get_all_field_names()


class UnitsOfTimeViewSet(viewsets.ModelViewSet):
    serializer_class = UnitsOfTimeSerializer
    queryset = UnitsOfTime.objects.all()
    filter_fields = UnitsOfTime._meta.get_all_field_names()


class IdentifierUseViewSet(viewsets.ModelViewSet):
    serializer_class = IdentifierUseSerializer
    queryset = IdentifierUse.objects.all()
    filter_fields = IdentifierUse._meta.get_all_field_names()


class IdentifierTypeViewSet(viewsets.ModelViewSet):
    serializer_class = IdentifierTypeSerializer
    queryset = IdentifierType.objects.all()
    filter_fields = IdentifierType._meta.get_all_field_names()


class ContactPointSystemViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPointSystemSerializer
    queryset = ContactPointSystem.objects.all()
    filter_fields = ContactPointSystem._meta.get_all_field_names()


class ContactPointUseViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPointUseSerializer
    queryset = ContactPointUse.objects.all()
    filter_fields = ContactPointUse._meta.get_all_field_names()


class AddressUseViewSet(viewsets.ModelViewSet):
    serializer_class = AddressUseSerializer
    queryset = AddressUse.objects.all()
    filter_fields = AddressUse._meta.get_all_field_names()


class AddressTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AddressTypeSerializer
    queryset = AddressType.objects.all()
    filter_fields = AddressType._meta.get_all_field_names()


class SignatureTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SignatureTypeSerializer
    queryset = SignatureType.objects.all()
    filter_fields = SignatureType._meta.get_all_field_names()


class NameUseViewSet(viewsets.ModelViewSet):
    serializer_class = NameUseSerializer
    queryset = NameUse.objects.all()
    filter_fields = NameUse._meta.get_all_field_names()


class QuantityComparatorViewSet(viewsets.ModelViewSet):
    serializer_class = QuantityComparatorSerializer
    queryset = QuantityComparator.objects.all()
    filter_fields = QuantityComparator._meta.get_all_field_names()


class AgeUnitsViewSet(viewsets.ModelViewSet):
    serializer_class = AgeUnitsSerializer
    queryset = AgeUnits.objects.all()
    filter_fields = AgeUnits._meta.get_all_field_names()


class NarrativeStatusViewSet(viewsets.ModelViewSet):
    serializer_class = NarrativeStatusSerializer
    queryset = NarrativeStatus.objects.all()
    filter_fields = NarrativeStatus._meta.get_all_field_names()
