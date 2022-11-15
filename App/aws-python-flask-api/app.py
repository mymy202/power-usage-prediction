from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello world!')


@app.route("/hello")
def hello():
    name = request.args.get("name")
    message = "Hello {0}!".format(name)
    return jsonify(message)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
