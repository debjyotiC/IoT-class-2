from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
app.debug = True


@app.route('/update', methods=['GET'])
def update():
    parser = reqparse.RequestParser()
    parser.add_argument('api_key', type=str)
    parser.add_argument('field1', type=float)
    data = parser.parse_args()
    print(data)
    return '200'


if __name__ == '__main__':
    app.run()
