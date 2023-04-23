from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2cu3n9d29u3nc29'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('./ChatPage.html')

@socketio.on('Evento 1')
def handle_event(json):
    print('Foi recebido uma mensagem:' + str(json))
    socketio.emit('Minha resposta', json)

if __name__ == '__main__':
    socketio.run(app, debug = True)