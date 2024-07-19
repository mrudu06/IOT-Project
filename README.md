# temp_control_iot
This is a simple IOT project using Raspberry pi (https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)and DHT22 sensor(https://www.instructables.com/How-to-use-DHT-22-sensor-Arduino-Tutorial/).The data recieved is then publishes in the form of a table and bar graph using [Python Flask] (http://flask.pocoo.org/) and [PostgreSQL](https://www.postgresql.org/).

## Installation

### Prerequisites

- Raspberry Pi with Raspbian OS
- DHT22 Sensor
- Python 3.7+
- PostgreSQL

### Hardware Setup

1. Connect the DHT22 sensor to the Raspberry Pi:
   - VCC to 3.3V
   - GND to GND
   - Data to GPIO pin (e.g., GPIO17)

### Software Setup

1. Clone the repository
    ```shell
    git clone https://github.com/yourusername/raspberry-pi-dht22.git
    ```
2. Navigate to the project directory
    ```shell
    cd raspberry-pi-dht22
    ```
3. Set up a Python virtual environment and activate it
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install Python dependencies
    ```shell
    pip install -r requirements.txt
    ```
5. Set up the PostgreSQL database
    ```shell
    sudo -u postgres psql
    CREATE DATABASE iot;
    CREATE USER pi WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE iot TO pi;
    \q
    ```
6. Update the database configuration in `config.py`
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://pi:password@localhost/sensor_data'
    ```

## Usage

1. Run the data collection script to read data from the DHT22 sensor and store it in PostgreSQL
    ```shell
    python data_collector.py
    ```
2. Run the Flask web application to display the data
    ```shell
    python app.py
    ```
3. Open a web browser and navigate to `http://<your-raspberry-pi-ip>:5000` to view the data.

## Features

- Collects temperature and humidity data using a DHT22 sensor.
- Stores the data in a PostgreSQL database.
- Displays the data in a table and bar graph using a Flask web application.

## Project Structure


