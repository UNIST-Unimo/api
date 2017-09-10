from flask import Flask
from flask_restful import Resource, Api
from app.modules.user.resource import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
