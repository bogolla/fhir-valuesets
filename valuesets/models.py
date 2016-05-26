"""Valueset models."""
import uuid
from django.db import models


class ValuesetBase(models.Model):
    """Base Model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True)
    display = models.CharField(max_length=255)
    definition = models.TextField(null=True, blank=True)

    class Meta:
        """meta class."""
        abstract = True

    def __str__(self):
        """repr."""
        return self.display


class TimingAbbreviation(ValuesetBase):
    """TimingAbbreviation."""
    pass


class EventTiming(ValuesetBase):
    """event-timing."""
    pass


class UnitsOfTime(ValuesetBase):
    """units-of-time."""
    pass


class IdentifierUse(ValuesetBase):
    """identifier-use."""
    pass


class IdentifierType(ValuesetBase):
    """identifier-type."""
    pass


class ContactPointSystem(ValuesetBase):
    """contact-point-system"""
    pass


class ContactPointUse(ValuesetBase):
    """contact-point-use"""
    pass


class AddressUse(ValuesetBase):
    """address-use"""
    pass


class AddressType(ValuesetBase):
    """address-type"""
    pass


class SignatureType(ValuesetBase):
    """signature-type"""
    pass


class NameUse(ValuesetBase):
    """name-use"""
    pass


class QuantityComparator(ValuesetBase):
    """quantity-comparator"""
    pass


class AgeUnits(ValuesetBase):
    """age-units"""
    pass


class NarrativeStatus(ValuesetBase):
    """narrative-status."""
    pass


class OrganizationType(ValuesetBase):
    """organization-type"""
    pass


class ContactentityType(ValuesetBase):
    """contactentity-type"""
    pass
