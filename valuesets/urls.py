"""routers."""
from rest_framework import routers
from .views import (
    TimingAbbreviationViewSet,
    EventTimingViewSet,
    UnitsOfTimeViewSet,
    IdentifierUseViewSet,
    IdentifierTypeViewSet,
    ContactPointSystemViewSet,
    ContactPointUseViewSet,
    AddressUseViewSet,
    AddressTypeViewSet,
    SignatureTypeViewSet,
    NameUseViewSet,
    QuantityComparatorViewSet,
    AgeUnitsViewSet,
    NarrativeStatusViewSet
)

router = routers.SimpleRouter()
router.register(r'timing_abbreviation', TimingAbbreviationViewSet)
router.register(r'event_timing', EventTimingViewSet)
router.register(r'units_of_time', UnitsOfTimeViewSet)
router.register(r'identifier_use', IdentifierUseViewSet)
router.register(r'identifier_type', IdentifierTypeViewSet)
router.register(r'contact_point_system', ContactPointSystemViewSet)
router.register(r'contact_point_use', ContactPointUseViewSet)
router.register(r'address_use', AddressUseViewSet)
router.register(r'address_type', AddressTypeViewSet)
router.register(r'signature_type', SignatureTypeViewSet)
router.register(r'name_use', NameUseViewSet)
router.register(r'quantity_comparator', QuantityComparatorViewSet)
router.register(r'age_unit', AgeUnitsViewSet)
router.register(r'narrative_status', NarrativeStatusViewSet)

urlpatterns = router.urls
