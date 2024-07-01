#!/usr/bin/env python
# coding: utf-8
#Auther: Ranveer Chaudhary

import CipherAnalyzer
CipherAnalyzer.init()

from flask import url_for, render_template, Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

password = ""

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/config', methods= ["POST"])
def config():
    global password
    if(request.method == "POST"):
        data = request.get_json()
        password = data['password']
        
    return ({"message": "success"})


@app.route("/analyzer", methods= ["GET"])
def analyze():
    global password
    strength = CipherAnalyzer.analyze(password)
    return jsonify({"strength": strength})


if __name__ == '__main__':
    app.run(debug=False)

