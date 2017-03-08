# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 11:20:00 2016

@author: AustinPeel
"""

import requests 

headers = {'api_key': 'INSERT_API_KEY',}
API_URL = "https://api.wmata.com"

 
def getBusIncidents():
  url = API_URL + "/Incidents.svc/json/BusIncidents"
  r = requests.get(url, headers=headers)
  return r.json()
  

def getBusPosition(routeID=None, lat=None, lon=None, radius=None):
   url = API_URL + "/Bus.svc/json/jBusPositions"
   payload = {'RouteID': routeID, 'Lat': lat, 'Lon': lon, 'Radius': radius}  
   r = requests.get(url, headers=headers, params=payload)
   return r.json()

#For a given date, returns the set of ordered latitude/longitude points along 
#a route variant along with the list of stops served.  
def getBusRouteDetails(routeID,date=None): 
   url = API_URL + "/Bus.svc/json/jRouteDetails"
   payload = {'RouteID': routeID, 'Date': date}  
   r = requests.get(url, headers=headers, params=payload)
   return r.json()
   
#Returns a list of all bus route variants (patterns). 
#For example, the 10A and 10Av1 are the same route, but may stop at slightly different locations.
def getBusAlternateRoutes():
   url = API_URL + "/Bus.svc/json/jRoutes"
   r = requests.get(url, headers=headers)
   return r.json()

#Returns schedules for a given route variant for a given date.
def getBusRouteSchedule(routeID,date=None,variations=False): 
   url = API_URL + "/Bus.svc/json/jRouteSchedule"
   payload = {'RouteID': routeID, 'Date': date,'IncludingVariations': variations} 
   r = requests.get(url, headers=headers, params=payload)
   return r.json()
   
#Returns a set of buses scheduled at a stop for a given date.
def getBusStopSchedule(stopID,date=None): 
   url = API_URL + "/Bus.svc/json/jStopSchedule"
   payload = {'stopID': stopID, 'Date': date}  
   r = requests.get(url, headers=headers, params=payload)
   return r.json()

#returns a list of nearby bus stops based on latitude, longitude, and radius. Omit all parameters to retrieve a list of all stops.      
def getBusStops(lat=None, lon=None, radius=None):
   url = API_URL + "/Bus.svc/json/jStops"
   payload = {'Lat': lat, 'Lon': lon, 'Radius': radius}  
   r = requests.get(url, headers=headers, params=payload)
   return r.json()   


def getRailLineInfo():
  url = API_URL + "/Rail.svc/json/jLines"
  r = requests.get(url, headers=headers)
  return r.json()
  
#Returns parking information at a station based on a given StationCode. Omit the StationCode to return parking information for all stations.
def getRailParkingInfo(station=None):
    url = API_URL + "/Rail.svc/json/jStationParking" 
    payload = {'StationCode': station}  
    r = requests.get(url, headers=headers, params=payload)
    return r.json()

def getRailElevatorIncidents(station=None):
  url = API_URL + "/Incidents.svc/json/ElevatorIncidents" 
  payload = {'StationCode': station}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()


def getRailIncidents():
   url = API_URL + "/Incidents.svc/json/Incidents"
   r = requests.get(url, headers=headers)
   return r.json()

def getRailPath(startStation,endStation):
  url = API_URL + "/Rail.svc/json/jPath" 
  payload = {'FromStationCode': startStation,'ToStationCode' : endStation}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()
  
#Returns a list of nearby station entrances based on latitude, longitude, and radius (meters). Omit search parameters to return all station entrances.
def getRailStations(lat=None, lon=None, radius=None):
  url = API_URL + "/Rail.svc/json/jStationEntrances" 
  payload = {'Lat': lat, 'Lon': lon, 'Radius': radius}   
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns station location and address information based on a given StationCode.
def getRailStationInfo(station):
  url = API_URL + "/Rail.svc/json/jStationInfo" 
  payload = {'StationCode': station}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns a list of station location and address information based on a given LineCode
def getRailStationList(line=None):
  url = API_URL + "/Rail.svc/json/jStations" 
  payload = {'LineCode': line}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns opening and scheduled first/last train times based on a given StationCode
def getRailStationTimes(station=None):
  url = API_URL + "/Rail.svc/json/jStationTimes" 
  payload = {'StationCode': station}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns a distance, fare information, and estimated travel time between any two stations, including those on different lines. 
def getRailPathInfo(startStation=None,endStation=None):
  url = API_URL + "/Rail.svc/json/jSrcStationToDstStationInfo" 
  payload = {'FromStationCode': startStation,'ToStationCode' : endStation}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns next bus arrival times at a stop.
def getBusPredictions(stopID):
  url = API_URL + "/NextBusService.svc/json/jPredictions" 
  payload = {'stopID': stopID}  
  r = requests.get(url, headers=headers, params=payload)
  return r.json()

#Returns next train arrival information for one or more stations.
def getRailPredictions(station="All"):
  url = API_URL + "/StationPrediction.svc/json/GetPrediction/" +station +"/"
  r = requests.get(url, headers=headers)
  return r.json()


