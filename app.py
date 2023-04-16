import time
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import RPi.GPIO as GPIO

# Raspberry Pi hardware SPI configuration.
SPI_PORT = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Configure the Raspberry Pi GPIO for the button
BUTTON_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

polling = False
temperature_data = []

@app.route('/')
def index():
    return render_template('index.html', title="Tim's Beanery")

@app.route('/toggle')
def toggle():
    global polling
    polling = not polling
    return '', 204

@socketio.on('connect', namespace='/beanery')
def handle_connect():
    global polling
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if not button_state:
            polling = not polling
            time.sleep(0.5)
        if polling:
            temp_c = sensor.readTempC()
            temperature_data.append(temp_c)
            socketio.emit('temperature_data', {'temp': temp_c, 'time': len(temperature_data)}, namespace='/beanery')
        time.sleep(1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
