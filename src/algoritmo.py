"""
Módulo de implementação do algoritmo EDF (Earliest Deadline First).
Responsável pela lógica de minimização de atraso máximo.
"""


def minimizar_atraso(tarefas, hora_inicio=0.0):
    """
    Algoritmo EDF (Earliest Deadline First) para minimizar o atraso máximo.
    
    Args:
        tarefas: Lista de dicts com {'nome', 'duracao', 'deadline', 'cliente', 'prioridade'}
        hora_inicio: Tempo de início do expediente/logística (float)
    
    Returns:
        tuple: (cronograma com detalhes, atraso_maximo, tempo_total, atrasos_individuais)
    """
    # Ordena as tarefas por deadline (Earliest Deadline First)
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['deadline'])
    
    tempo_atual = hora_inicio
    cronograma = []
    atraso_maximo = 0
    atrasos_individuais = []
    
    for t in tarefas_ordenadas:
        inicio = tempo_atual
        fim = inicio + t['duracao']
        atraso = max(0, fim - t['deadline'])
        
        if atraso > atraso_maximo:
            atraso_maximo = atraso
            
        cronograma.append({
            'nome': t['nome'],
            'cliente' : t.get('cliente', 'N/A'),
            'prioridade': t.get('prioridade', 'Normal'),
            'duracao': t['duracao'],
            'inicio': inicio,
            'fim': fim,
            'deadline': t['deadline'],
            'atraso': atraso
        })
        
        atrasos_individuais.append({
            'nome': t['nome'],
            'cliente': t.get('cliente', 'N/A'),
            'atraso': atraso
        })
        
        tempo_atual = fim
        
    return cronograma, atraso_maximo, tempo_atual, atrasos_individuais
