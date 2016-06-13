"""routers."""
from rest_framework import routers
from ..views import (
    TimingAbbreviationViewSet,
    EventTimingViewSet,
    UnitsOfTimeViewSet,
    SignatureTypeViewSet,
    AgeUnitsViewSet
)

router = routers.SimpleRouter()
router.register(
    r'timing_abbreviation', TimingAbbreviationViewSet, 'timing_abbreviation')
router.register(r'event_timing', EventTimingViewSet, 'event_timing')
router.register(r'units_of_time', UnitsOfTimeViewSet, 'units_of_time')
router.register(r'signature_type', SignatureTypeViewSet, 'signature_type')
router.register(r'age_unit', AgeUnitsViewSet, 'age_unit')
urlpatterns = router.urls
