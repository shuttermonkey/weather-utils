#!/usr/bin/python3

#print("purpose is to download weather information and save every hour as e.g. mon-1pm-grid.json or mon-5am-hourly.json")
import os # used for evironment variables 
from dotenv import load_dotenv
load_dotenv()

import urllib.request
#from urllib.error import HTTPError
import json

from datetime import date, datetime, timedelta, timezone
import pytz


def getURLdata(url):
    try:
        operUrl = urllib.request.urlopen(url)
        if(operUrl.getcode()==200):
            data = operUrl.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", operUrl.getcode())
            jsonData = {'status': 'failure to retrieve'}
    except:
        jsonData = {'status': 'error: failure to retrieve'}
        print(jsonData['status'])
    return jsonData

def writeFile(filedata, myfilename):
    if (len(filedata)) > 1:
        with open(myfilename, 'w') as outfile:
            json.dump(filedata, outfile)

def main():
    eastern = pytz.timezone("US/Eastern")
    dtnow = eastern.localize(datetime.now())
    fdt = dtnow.strftime("%a-%I%p")
    homeDir = os.environ.get("WUTILFILEPATH")
    #print(homeDir)
    hourData = "https://api.weather.gov/gridpoints/OKX/47,53/forecast/hourly"      
    gridData = "https://api.weather.gov/gridpoints/OKX/47,53"

    hourInfo = getURLdata(hourData)
    writeFile(hourInfo,homeDir + fdt+"-hour.json")

    gridInfo = getURLdata(gridData)
    writeFile(gridInfo,homeDir + fdt+"-grid.json")

if __name__ == "__main__":
    main()

#print(os.environ)

