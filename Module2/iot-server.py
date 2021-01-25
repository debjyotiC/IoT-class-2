from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import datetime
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test_DB"]
mycol = mydb["sensor_data"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/update', methods=['GET'])
def update():
    parser = reqparse.RequestParser()
    parser.add_argument('api_key', type=str)
    parser.add_argument('field1', type=float)

    data = parser.parse_args()
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data['date'] = date
    print(data)
    mycol.insert_one(data)
    return '200 OK'


if __name__ == '__main__':
    app.run(host='192.168.0.107')
