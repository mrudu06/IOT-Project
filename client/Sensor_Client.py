import requests
import Adafruit_DHT as dht
from time import sleep

while True:

    url = 'http://192.168.0.102:5000/sensors'
    headers = {'Content-Type': 'application/json'}
    DHT_PIN = 17

    h, t = dht.read_retry(dht.DHT22, DHT_PIN)


    if h is not None and t is not None:
        data = {
            "name": "DHT22",
            "temperature": t,
            "humidity": h
        }

        response = requests.post(url, headers=headers, json=data)

        if  ( 200<= response.status_code <= 300):
            print('Data posted successfully:')
        else:
            print('Failed to post data:', response.status_code, response.text)
    else:
        print('Failed to get reading from the sensor. Try again!')
        
    sleep(10)
