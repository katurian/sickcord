import requests 
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = 'thxh8o43b83XXXXXXXXXXXXXXXXXX'

def getMarkersInRadius(lat, lon, ids, limit, radius, date_start, date_end):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/markers/getMarkersInRadius.php?lat={lat}&lon={lon}&ids={ids}&limit={limit}&radius={radius}&date_start={date_start}&date_end={date_end}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def markerCountInRadius(lat, lon, ids, limit, radius, date_start, date_end):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/markers/getMarkerCountInRadius.php?lat={lat}&lon={lon}&ids={ids}&radius={radius}&date_start={date_start}&date_end={date_end}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getForecast(loc, lat, lon):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/maps/getForecast.php?loc={loc}&lat={lat}&lon={lon}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getWeatherMaps(ids):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/maps/getWeathermaps.php?id={ids}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getIllnesses():
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/illnesses/getIllnesses.php?api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getSickScoreInRadius(lat, lon):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/markers/getMarkersInRadius.php?lat={lat}&lon={lon}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getSickScoreByZipcode(country, zipcode, ids):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/sickscore/getSickScoreByZipcode.php?country={country}&zip={zipcode}&ids={ids}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getColdFluScoreInRadius(lat, lon):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/markers/getMarkersInRadius.php?lat={lat}&lon={lon}&ids={ids}&limit={limit}&radius={radius}&date_start={date_start}&date_end={date_end}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getAllergySickScoreInRadius(lat, lon):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/sickscore/getAllergySickScoreInRadius.php?lat={lat}&lon={lon}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON

def submitReport(lat, lon, ids, report, temp):
    r = requests.get(f'https://mobilesvc.sickweather.com/ws/v2.0/reporting/submitReport.php?lat={lat}&lon=3{lon}&id={ids}&report={report}&temp={temp}&api_key={api_key}', verify=False)
    resultJSON = r.json()
    return resultJSON
