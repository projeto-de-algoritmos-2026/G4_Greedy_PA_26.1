from flask import Flask, request, jsonify, render_template
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from algoritmo import minimizar_atraso

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    tarefas = data.get('tarefas', [])
    hora_inicio = float(data.get('hora_inicio', 0.0))
    
    cronograma, atraso_maximo, hora_fim, atrasos_individuais = minimizar_atraso(tarefas, hora_inicio)
    
    return jsonify({
        'cronograma': cronograma,
        'atraso_maximo': atraso_maximo,
        'tempo_total': hora_fim - hora_inicio,
        'hora_fim': hora_fim,
        'hora_inicio': hora_inicio,
        'atrasos_individuais': atrasos_individuais
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)