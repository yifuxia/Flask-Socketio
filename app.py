import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

import time

import socketio
import eventlet
from flask import Flask, render_template, send_from_directory

from GetData import get_duration, get_published_hour, get_num_words_in_title, get_published_day_of_week, get_words

sio = socketio.Server()
app = Flask(__name__, static_url_path='')

app.config['DEBUG'] = True # enable hot reload

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 3001)), app)
