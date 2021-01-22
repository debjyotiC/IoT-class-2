from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/update', methods=['GET'])
def update():
    parser = reqparse.RequestParser()
    parser.add_argument('api_key', type=str)
    parser.add_argument('field1', type=float)

    data = parser.parse_args()

    print(data)

    return ''


if __name__ == '__main__':
    app.run(host='192.168.0.107')
