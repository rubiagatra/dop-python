from flask import Flask, jsonify, request
from jsonschema import validate
from schema import request_schema
from search import search_user

app = Flask(__name__)
        

@app.route("/search", methods=["GET"])
def search():
    try:
        validate(request.args, schema=request_schema)
    except:
        return jsonify({"error": "bad request"}), 400

    try:
        user_response = search_user(request.args["first_name"])
    except Exception as e:
        return jsonify({"error": repr(e)}), 500 

    return jsonify(user_response), 200 



app.run("localhost", port=5000, debug=True)
