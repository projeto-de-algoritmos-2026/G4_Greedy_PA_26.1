# G4_Greedy_PA_26.1

## Nome do Projeto

SLA Optimizer (EDF)

Conteúdo da Disciplina: Algoritmos Ambiciosos <br>

## Alunos

| Matrícula  | Aluno                               |
| ---------- | ----------------------------------- |
| 23/1027032 | Arthur Evangelista de Oliveira      |
| 23/1038303 | Yan Matheus Santa Brigida de Aguiar |

## Link da gravação

[Assista ao vídeo no Youtube]()

## Sobre

Aplicação web que implementa o algoritmo **Earliest Deadline First (EDF)** para otimizar agendamento de tarefas minimizando o atraso máximo em um sistema de SLA (Service Level Agreement). O projeto permite adicionar tarefas com duração e deadline, e calcula a ordem ideal de execução para minimizar atrasos.

## Screenshots

![screenshot1]()
![screenshot2]()
![screenshot3]()

## Instalação

Linguagem: **Python 3.10+**<br>
Framework (Web): **Flask**<br>

**Passo a passo (Linux/Mac/Windows):**

1. Criar e ativar virtualenv:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Executar o servidor:

```bash
python app.py
```

4. Acessar a interface em `http://localhost:5000`

## Funcionalidades

- Interface web para adicionar tarefas (título, duração, deadline)
- Algoritmo EDF (Earliest Deadline First) para minimizar atraso máximo
- Exibição de cronograma detalhado por tarefa
- Cálculo de atraso máximo e tempo total
- API JSON (`POST /calcular`) para integração programática

## Estrutura do Projeto

```
.
├── app.py                    # Servidor Flask e endpoints
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
├── src/
│   ├── __init__.py
│   ├── algoritmo.py          # Implementação do EDF
│   ├── display.py            # Funções de exibição
├── templates/
│   └── index.html            # Interface web
└── static/
    ├── css/
    │   └── style.css         # Estilos da UI
    └── js/
        └── scripts.js        # Lógica frontend
```

## Outros

Projeto desenvolvido para a disciplina de Projeto de Algoritmos (UnB), com foco em algoritmos ambiciosos (greedy).
