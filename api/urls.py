from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('api/hitgood', hitGood),
    path('api/hitverygood', hitVeryGood),
    path('api/hitbad', hitBad),
    path('api/hitaverage', hitAverage),
    path('api/hitverybad', hitVeryBad),
    path('check/', check)
]