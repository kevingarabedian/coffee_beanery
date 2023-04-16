# Tim's Beanery

Tim's Beanery is a Raspberry Pi-based coffee bean roaster monitoring system. It uses a MAX31855 thermocouple amplifier and a K-type thermocouple to measure the temperature. The system logs the temperature data in memory and displays it on a live graph via a web interface. The temperature polling can be toggled on and off using a button on the webpage or a physical button connected to the Raspberry Pi.

## Setup Instructions

1. Install required Python libraries:

pip install Flask flask_socketio eventlet matplotlib adafruit-circuitpython-max31855 RPi.GPIO

2. Clone this repository or create the following files in a new directory:

* `app.py`: The main Flask application
* `templates/index.html`: The web interface

3. Copy the contents provided in the previous responses for `app.py` and `templates/index.html`.

4. Connect the MAX31855 thermocouple amplifier to the Raspberry Pi's SPI pins and the K-type thermocouple to the MAX31855.

5. Connect a button to the Raspberry Pi's GPIO pins (the example uses BCM pin 18). Ensure the button is connected to the appropriate GPIO pin and ground with a pull-up resistor if needed.

6. Customize the pin configuration, SPI settings, and GPIO settings in the `app.py` file according to your hardware setup.

7. Run the Flask app:

python app.py

8. Access the web interface on any device connected to the same network as the Raspberry Pi by navigating to the Raspberry Pi's IP address with port 5000 (e.g., `http://192.168.1.100:5000`).

Summary:

- Raspberry Pi 3 Model B
- MAX31855 thermocouple amplifier
- K-type thermocouple
- Python Flask web app
- Real-time temperature graph
- Physical and web-based buttons to toggle temperature polling
