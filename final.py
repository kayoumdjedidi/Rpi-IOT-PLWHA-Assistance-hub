import thingspeak
import time
import Adafruit_DHT
import requests

channel_id = 1966402 # put here the ID of the channel you created before
writekey = 'H0NR1QMUUEEZCV7J' # update the "WRITE KEY"

pin = 23
sensor = Adafruit_DHT.DHT11

def measure():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Did not receive any reading from sensor. Please check!')
        # update the value
        #response = channel.update({'field1': temperature, 'field2': humidity})
        requests.get('https://api.thingspeak.com/update?api_key={key}&field1={h}&field2={t}'.format(h=humidity, t=temperature, key= writekey))
    except Exception as e:
        #print("connection failure")
        print(e.args)

if __name__ == "__main__":
        #channel = thingspeak.Channel(id=channel_id)
        while True:
            measure()
        #free account has a limitation of 15sec between the updates
            time.sleep(0.5)
