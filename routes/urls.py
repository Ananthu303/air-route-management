from django.urls import path
from .views import (
    AddAirportRouteView,
    FindNthNodeView,
    LongestNodeView,
    ShortestDurationView,
)

urlpatterns = [
    path("add/", AddAirportRouteView.as_view(), name="add_airport_route"),
    path("find-nth/", FindNthNodeView.as_view(), name="find_nth_node"),
    path("longest/", LongestNodeView.as_view(), name="longest_node"),
    path("shortest/", ShortestDurationView.as_view(), name="shortest_duration"),
]
