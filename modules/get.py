# Loop to fetch new DELAY data from Huxley

import requests
import json

def get (origin, destination, huxley):
    trains = [] # creates an empty list to store the data
    for o in origin: # iterates through each possible pair of origins and destinations from the lists passed to the function
        for d in destination:
            url = ('https://'+huxley+'/delays/'+o+'/to/'+d) # creates url to fetch the data
            #print (url)
            response = requests.get(url) # stores response as 'response'
            data = json.loads(response.text) # converts from json to text
            #Prettyprint data for debugging
            #print(json.dumps(data, indent=4, sort_keys=True))
            # append new data to 'data' as a list of dicts, tailoring what information is stored based on the delay status from Huxley
            if data['delays'] == True and data['totalDelayMinutes'] > 0:
                trains.append({"origin": o, "destination": d, "string": "Delays", "delay": 0, "delayMinutes": data["totalDelayMinutes"]})
            elif data['totalTrains'] == 0:
                trains.append({"origin": o, "destination": d, "string": "No Service", "delay": 2})
            else:
                trains.append({"origin": o, "destination": d, "string": "Good Service", "delay": 1})
    return trains