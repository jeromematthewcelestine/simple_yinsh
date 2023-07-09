from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import random
from datetime import datetime
import os, psutil
import sys
from yinsh import yinsh


game = yinsh.YinshGame()
state = game.get_initial_state()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def route_index():
    return render_template('index.html')

@app.route('/state', methods = ['GET'])
def route_state():
    return jsonify(state)

@app.route('/action', methods = ['POST'])
def route_action():
    data = request.get_json()
    print(data)
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 7001, debug=True)