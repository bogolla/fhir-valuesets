"""valueset base serializers."""
from rest_framework import serializers
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
    QuantityComparator
)


class TimingAbbreviationSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = TimingAbbreviation


class EventTimingSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = EventTiming


class UnitsOfTimeSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = UnitsOfTime


class IdentifierUseSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = IdentifierUse


class IdentifierTypeSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = IdentifierType


class ContactPointSystemSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = ContactPointSystem


class ContactPointUseSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = ContactPointUse


class AddressUseSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = AddressUse


class AddressTypeSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = AddressType


class SignatureTypeSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = SignatureType


class NameUseSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = NameUse


class QuantityComparatorSerializer(serializers.ModelSerializer):

    class Meta:
        """meta class"""
        model = QuantityComparator
