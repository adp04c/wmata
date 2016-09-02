import wmata
#bus
wmata.getBusPosition(lon=-76.675302, lat= 39.191887,radius=10000)
wmata.getBusRouteDetails(routeID="B30")
wmata.getBusRouteSchedule(routeID="B30",variations=True)
wmata.getBusStopSchedule(stopID='3002579', date= '2016-06-06')
wmata.getBusStops(lon=-76.675302, lat= 39.191887,radius=10000)
wmata.getBusPredictions(1001195)

#rail
wmata.getRailPath("N06","N03")
wmata.getRailParkingInfo('F06')
wmata.getRailStations(lon=-76.675302, lat= 39.191887,radius=30000)
wmata.getRailIncidents()
wmata.getRailStationInfo("E10")
wmata.getRailStationList("RD")
wmata.getRailStationTimes("E10")
wmata.getRailPathInfo("J03","E10")
wmata.getRailPredictions()
