def minimizar_atraso(tarefas):
    # criei as tarefas como uma lista de dicts, yan [{'nome': 'Bug A', 'duracao': 2, 'deadline': 5}, ...]

    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['deadline'])
    
    tempo_atual = 0
    cronograma = []
    atraso_maximo = 0
    
    for t in tarefas_ordenadas:
        inicio = tempo_atual
        fim = inicio + t['duracao']
        atraso = max(0, fim - t['deadline'])
        
        if atraso > atraso_maximo:
            atraso_maximo = atraso
            
        cronograma.append({
            'nome': t['nome'],
            'inicio': inicio,
            'fim': fim,
            'deadline': t['deadline'],
            'atraso': atraso
        })
        
        tempo_atual = fim
        
    return cronograma, atraso_maximo