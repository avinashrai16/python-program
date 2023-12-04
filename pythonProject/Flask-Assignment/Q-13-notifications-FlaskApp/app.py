# app.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_notifications.html')

@socketio.on('connect', namespace='/chat')
def handle_connect():
    print('Client connected')
    emit('notification', {'message': 'Connected to the server'})

@socketio.on('disconnect', namespace='/chat')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('new_message', namespace='/chat')
def handle_new_message(message_data):
    sender = message_data['sender']
    message = message_data['message']

    # Simulate some processing time
    time.sleep(2)

    emit('notification', {'message': f'New message from {sender}: {message}'})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
