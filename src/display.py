"""
Módulo de exibição e análise dos resultados.
Responsável pela formatação e apresentação dos dados do algoritmo EDF.
"""


def exibir_cronograma(cronograma, atraso_maximo, tempo_total):
    """
    Exibe o cronograma de forma formatada com visualização clara.
    
    Args:
        cronograma: Lista de tarefas com informações de execução
        atraso_maximo: Maior atraso encontrado
        tempo_total: Tempo total de execução
    """
    print("\n" + "="*100)
    print("CRONOGRAMA DE EXECUÇÃO - SISTEMA DE SLA - MINIMIZAÇÃO DE ATRASO MÁXIMO (EDF)")
    print("="*100)
    print(f"\n{'ID':<10} {'Cliente':<12} {'Duracao':<10} {'Inicio':<8} {'Fim':<8} {'Deadline':<10} {'Atraso':<10} {'Status':<15}")
    print("-"*100)
    
    for item in cronograma:
        status = "No Prazo" if item['atraso'] == 0 else f"Atrasado {item['atraso']}h"
        print(f"{item['nome']:<10} {item['cliente']:<12} {item['duracao']:<10} {item['inicio']:<8} {item['fim']:<8} {item['deadline']:<10} {item['atraso']:<10} {status:<15}")
    
    print("-"*100)
    print(f"\nTempo Total de Execução: {tempo_total}h")
    print(f"Atraso Maximo: {atraso_maximo}h")
    print(f"\nResultado: Atraso maximo minimizado para {atraso_maximo}h\n")
    print("="*100 + "\n")


def analisar_atrasos(atrasos_individuais):
    """
    Analisa e exibe estatísticas dos atrasos.
    
    Args:
        atrasos_individuais: Lista de dicts com informações de atraso por tarefa
    """
    print("\n" + "="*100)
    print("ANÁLISE DE ATRASOS")
    print("="*100)
    
    atrasos_valores = [item['atraso'] for item in atrasos_individuais]
    no_prazo = sum(1 for a in atrasos_valores if a == 0)
    com_atraso = sum(1 for a in atrasos_valores if a > 0)
    
    print(f"\nTarefas no Prazo: {no_prazo}/10")
    print(f"Tarefas com Atraso: {com_atraso}/10")
    print(f"Atraso Medio: {sum(atrasos_valores) / len(atrasos_valores):.2f}h")
    print(f"Atraso Maximo: {max(atrasos_valores)}h")
    
    print("\n" + "-"*100)
    print("Detalhes por Tarefa:")
    print("-"*100)
    for item in atrasos_individuais:
        status = "No prazo" if item['atraso'] == 0 else "Com atraso"
        print(f"{item['nome']:<12} ({item['cliente']:<12}) - Atraso: {item['atraso']}h - [{status}]")
    
    print("\n" + "="*100 + "\n")
