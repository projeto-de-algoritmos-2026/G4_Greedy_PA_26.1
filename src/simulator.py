"""
Módulo de simulação (dados simulados removidos).

Este arquivo costumava conter dados de exemplo (simulados) e uma rotina
de execução da simulação. Para evitar dados hard-coded na aplicação, as
funções abaixo agora são placeholders que NÃO geram nem exibem dados por
padrão. Use a API/Web UI para fornecer tarefas ao algoritmo `minimizar_atraso`.
"""

def gerar_bugs_suporte(count: int = 0):
    """Retorna uma lista vazia (sem dados simulados).

    Parâmetros futuros podem permitir geração programática de dados,
    mas por ora não há dados hard-coded nesta aplicação.
    """
    return []


def simular_suporte_tecnico(bugs=None):
    """Placeholder: não executa a simulação automaticamente.

    Recebe opcionalmente uma lista de `bugs` (tarefas) e simplesmente a
    retorna. A lógica de execução e exibição deve ser acionada pela
    API/parte web (`app.py`) ou por scripts de teste separados.
    """
    if bugs is None:
        bugs = []
    return bugs
