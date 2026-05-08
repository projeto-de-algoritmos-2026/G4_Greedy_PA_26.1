"""
Módulo de simulação do sistema de suporte técnico.
Responsável pela geração de dados e execução da simulação.
"""

from algoritmo import minimizar_atraso
from display import exibir_cronograma, analisar_atrasos


def gerar_bugs_suporte():
    """
    Gera 10 bugs para o sistema de suporte técnico com prazos realistas.
    
    Returns:
        list: Lista de bugs com tempo estimado e deadline
    """
    bugs = [
        {'nome': 'Bug #001', 'cliente': 'Cliente A', 'duracao': 3, 'deadline': 8, 'prioridade': 'Alta'},
        {'nome': 'Bug #002', 'cliente': 'Cliente B', 'duracao': 2, 'deadline': 5, 'prioridade': 'Critica'},
        {'nome': 'Bug #003', 'cliente': 'Cliente C', 'duracao': 4, 'deadline': 12, 'prioridade': 'Normal'},
        {'nome': 'Bug #004', 'cliente': 'Cliente D', 'duracao': 1, 'deadline': 6, 'prioridade': 'Alta'},
        {'nome': 'Bug #005', 'cliente': 'Cliente E', 'duracao': 5, 'deadline': 15, 'prioridade': 'Normal'},
        {'nome': 'Bug #006', 'cliente': 'Cliente F', 'duracao': 2, 'deadline': 10, 'prioridade': 'Media'},
        {'nome': 'Bug #007', 'cliente': 'Cliente G', 'duracao': 3, 'deadline': 7, 'prioridade': 'Alta'},
        {'nome': 'Bug #008', 'cliente': 'Cliente H', 'duracao': 2, 'deadline': 9, 'prioridade': 'Media'},
        {'nome': 'Bug #009', 'cliente': 'Cliente I', 'duracao': 4, 'deadline': 14, 'prioridade': 'Normal'},
        {'nome': 'Bug #010', 'cliente': 'Cliente J', 'duracao': 2, 'deadline': 11, 'prioridade': 'Media'},
    ]
    return bugs


def simular_suporte_tecnico():
    """
    Simula o sistema completo de suporte técnico com o algoritmo EDF.
    """
    print("\n" + "="*100)
    print("SIMULAÇÃO: MINIMIZAÇÃO DE ATRASO MÁXIMO COM ALGORITMO EDF")
    print("="*100 + "\n")
    
    # Gera os bugs
    bugs = gerar_bugs_suporte()
    
    # Executa o algoritmo
    cronograma, atraso_maximo, tempo_total, atrasos = minimizar_atraso(bugs)
    
    # Exibe resultados
    exibir_cronograma(cronograma, atraso_maximo, tempo_total)
    analisar_atrasos(atrasos)
