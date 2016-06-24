"""viewsets file."""
from rest_framework import viewsets

from ..models import (
    TimingAbbreviation,
    EventTiming,
    UnitsOfTime,
    SignatureType,
    AgeUnits,
    GENERATED_MODELS
)

from ..serializers import (
    TimingAbbreviationSerializer,
    EventTimingSerializer,
    UnitsOfTimeSerializer,
    SignatureTypeSerializer,
    AgeUnitsSerializer
)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    hyperlinks = {
        valueset: reverse('valuesets:{0}-list'.format(valueset),
                          request=request,
                          format=format)
        for valueset in iter(GENERATED_MODELS)
    }

    return Response(hyperlinks)


class CommonViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **active** Valuesets in the server.

    You can perform any of the following operations in the server

    * GET all items: `/valuesets/Valuesets/`
    * GET item by id: `/valuesets/Valuesets/id`
    """
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
