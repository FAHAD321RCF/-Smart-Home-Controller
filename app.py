import Adafruit_DHT

# Set up sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin for DHT22 sensor

# WebSocket event to get temperature
@socketio.on('get_temperature')
def get_temperature():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if temperature is not None:
        temperature = round(temperature, 2)
        socketio.emit('temperature_update', {'temperature': temperature})
    else:
        socketio.emit('temperature_update', {'temperature': 'Error'})
