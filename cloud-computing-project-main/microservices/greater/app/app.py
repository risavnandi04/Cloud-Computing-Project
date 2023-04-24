from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_restful import Resource, Api
import math

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class greaterThan(Resource):
    def get(self, num1, num2):
        if num1 > num2:
            return {'result': num1}
        else:
            return {'result': num2}

api.add_resource(greaterThan, '/<string:num1>/<string:num2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )