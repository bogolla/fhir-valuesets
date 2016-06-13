from .urls import *  # noqa
from .generated_urls import *  # noqa

from .urls import urlpatterns as urlp
from .generated_urls import urlpatterns as urlg

urlpatterns = urlp + urlg
