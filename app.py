from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
socketio = SocketIO(app, async_mode='eventlet')
# Dicionário para contar votos
votos = {
    'vermelho': 0,
    'azul': 0
}

@app.route('/')
def index():
    return render_template('index.html', votos=votos)

@socketio.on('votar')
def handle_voto(data):
    carta = data.get('carta')
    if carta in votos:
        votos[carta] += 1
        print(f"Voto registrado para {carta}")
        socketio.emit('atualizar_votos', votos)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
