#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyroutelib3 import Router
import folium
router = Router("car")

depart = router.findNode(46.078025, 6.409053)
arrivee = router.findNode(46.193253,  6.234158)

status, route = router.doRoute(depart, arrivee)

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route))
    

c= folium.Map(location=[46.078025, 6.409053],zoom_start=10)
for coord in routeLatLons:
    coord=list(coord)
    folium.Marker(coord).add_to(c)
c.save('maCarte.html')