# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    """Example of how to send server-generated events to clients."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        number = random.randint(1, 100)
        socketio.emit('update', {'count': count, 'number': number}, namespace='/test')

@socketio.on('connect', namespace='/test')
def test_connect():
    """Client is connected."""
    print('Client connected')
    emit('update', {'count': 0, 'number': 0})

if __name__ == '__main__':
    socketio.start_background_task(target=background_thread)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
