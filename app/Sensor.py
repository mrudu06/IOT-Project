from flask import Flask, request,jsonify,render_template
import psycopg2
from decimal import Decimal
from datetime import datetime

app = Flask(__name__)

host = "127.0.0.1"
port = "5432"
database = "iot"
user = "postgres"
password = "2006"

def get_db_connection():
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    return connection

def convert_decimal_to_float(data):
    if isinstance(data, list):
        return [convert_decimal_to_float(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(convert_decimal_to_float(item) for item in data)
    elif isinstance(data, dict):
        return {key: convert_decimal_to_float(value) for key, value in data.items()}
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sensors', methods=['POST'])
def add_sensor_data():
    connection = get_db_connection()
    cursor = connection.cursor()

    data = request.get_json()

    # s_no = request.form['s_no']
    name = data.get('name')
    temperature = data.get('temperature')
    humidity = data.get ('humidity')

    query = "INSERT INTO SENSOR(name, temperature, humidity) VALUES ( %s, %s, %s)"
    values = (name, temperature, humidity)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return "Data inserted successfully", 201



@app.route('/sensors', methods=['GET'])
def get_sensor_data():
    print("get_sensor")
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM SENSOR")
    rows = cursor.fetchall()
    print (rows)
    converted_rows = convert_decimal_to_float(rows)
    print(converted_rows)


    datalist =[]
    response = ""
    for row in converted_rows:
        data = {}
        data["serial_no"] = row[0]
        data["name"]=row[1]
        data['temperature']=row[2]
        data["humidity"]=row[3]
        data["timestamp"] = row[4]
        datalist.append(data)
    

    cursor.close()
    connection.close()

    return jsonify(datalist),200


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
