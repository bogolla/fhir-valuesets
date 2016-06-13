"""valueset base serializers."""
from rest_framework import serializers
from ..models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    SignatureType,
    AgeUnits,
)


class TimingAbbreviationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimingAbbreviation


class EventTimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTiming


class UnitsOfTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitsOfTime


class SignatureTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignatureType


class AgeUnitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgeUnits
