let tasks = [];

document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskListContainer = document.getElementById('task-list');
    const taskCountBadge = document.getElementById('task-count');
    const calculateBtn = document.getElementById('calculate-btn');

    // Panels
    const placeholderState = document.getElementById('placeholder-state');
    const resultsPanel = document.getElementById('results-panel');

    // Result elements
    const ganttChart = document.getElementById('gantt-chart');
    const resultsTableBody = document.querySelector('#results-table tbody');

    // Mapeamento visual das cores para facilitar feedback
    let taskIdCounter = 0;

    // Add task
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const nameInput = document.getElementById('task-name');
        const durationInput = document.getElementById('task-duration');
        const deadlineInput = document.getElementById('task-deadline');

        taskIdCounter++;
        const task = {
            id: taskIdCounter,
            nome: nameInput.value.trim(),
            duracao: parseFloat(durationInput.value),
            deadline: parseFloat(deadlineInput.value)
        };

        tasks.push(task);
        renderTaskList();

        // Reset form
        nameInput.value = '';
        durationInput.value = '';
        deadlineInput.value = '';
        nameInput.focus();

        updateState();
    });

    // Render "Kanban" List
    function renderTaskList() {
        taskListContainer.innerHTML = '';

        if (tasks.length === 0) {
            taskListContainer.innerHTML = `
                <div class="empty-state">
                    <i class="fa-solid fa-inbox"></i>
                    <p>Nenhuma tarefa no backlog.</p>
                </div>
            `;
            return;
        }

        tasks.forEach((task) => {
            const card = document.createElement('div');
            card.className = 'task-card';
            card.innerHTML = `
                <div class="task-card-header">
                    <div class="task-card-title">${task.nome}</div>
                    <button type="button" class="btn-remove" onclick="removeTask(${task.id})" title="Remover">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>
                <div class="task-card-metrics">
                    <div class="task-metric" title="Duração">
                        <i class="fa-regular fa-clock"></i> ${task.duracao}h
                    </div>
                    <div class="task-metric" title="Prazo (Deadline)">
                        <i class="fa-regular fa-calendar-check"></i> ${task.deadline}h
                    </div>
                </div>
            `;
            taskListContainer.appendChild(card);
        });

        // Scroll automatically to bottom of the list when new item added
        taskListContainer.scrollTop = taskListContainer.scrollHeight;
    }

    // Remove Task global function
    window.removeTask = function (id) {
        tasks = tasks.filter(t => t.id !== id);
        renderTaskList();
        updateState();
    };

    function updateState() {
        taskCountBadge.textContent = tasks.length;
        calculateBtn.disabled = tasks.length === 0;

        if (tasks.length === 0) {
            resultsPanel.style.display = 'none';
            placeholderState.style.display = 'flex';
        }
    }

    // Calculate Schedule via API
    calculateBtn.addEventListener('click', async () => {
        const originalHTML = calculateBtn.innerHTML;
        calculateBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Processando...';
        calculateBtn.disabled = true;

        const startTimeInput = document.getElementById('start-time');
        const startTime = parseFloat(startTimeInput.value) || 0;

        try {
            const response = await fetch('/calcular', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ tarefas: tasks, hora_inicio: startTime })
            });

            if (!response.ok) throw new Error('Falha na resposta do servidor.');

            const data = await response.json();

            setTimeout(() => {
                renderResults(data);
                calculateBtn.innerHTML = originalHTML;
                calculateBtn.disabled = false;
            }, 600); // Artificial delay to show processing state visually

        } catch (error) {
            console.error('Erro:', error);
            alert('Não foi possível calcular o cronograma. Verifique se o servidor Flask está rodando.');
            calculateBtn.innerHTML = originalHTML;
            calculateBtn.disabled = false;
        }
    });

    // Render output in the Main Content area
    function renderResults(data) {
        placeholderState.style.display = 'none';
        resultsPanel.style.display = 'block';

        // Update Highlights
        document.getElementById('max-lateness').textContent = `${data.atraso_maximo}h`;
        document.getElementById('total-time').textContent = `${data.tempo_total}h (Termina às ${data.hora_fim}h)`;

        // Render Gantt Chart
        ganttChart.innerHTML = '';
        const totalDuration = data.tempo_total || 1;

        data.cronograma.forEach(task => {
            const widthPercentage = (task.duracao / totalDuration) * 100;
            const block = document.createElement('div');
            block.className = `gantt-block ${task.atraso > 0 ? 'late' : 'on-time'}`;
            // Mínimo de largura para o bloco n ficar invisível
            block.style.width = widthPercentage < 2 ? '2%' : `${widthPercentage}%`;

            if (widthPercentage > 15) {
                block.innerHTML = `<span>${task.nome}</span>`;
            } else if (widthPercentage > 8) {
                block.innerHTML = `<span>${task.nome.substring(0, 3)}...</span>`;
            }

            // O tooltip flutuante (agora posicionado no topo para n cortar c/ overflow)
            const tooltip = document.createElement('div');
            tooltip.className = 'gantt-info';

            const tooltipStatus = task.atraso > 0
                ? `<span style="color:#fca5a5"><i class="fa-solid fa-triangle-exclamation"></i> Atraso: ${task.atraso}h</span>`
                : `<span style="color:#86efac"><i class="fa-solid fa-check"></i> No Prazo</span>`;

            tooltip.innerHTML = `
                <div style="font-weight:700; margin-bottom:4px; font-size:14px">${task.nome}</div>
                <div>Execução: <strong>${task.inicio}h até ${task.fim}h</strong></div>
                <div>Prometido até: <strong>${task.deadline}h</strong></div>
                <div style="margin-top:4px; border-top:1px solid #475569; padding-top:4px">Status: ${tooltipStatus}</div>
            `;

            block.appendChild(tooltip);
            ganttChart.appendChild(block);
        });

        // Render detailed Table
        resultsTableBody.innerHTML = '';
        data.cronograma.forEach((task, index) => {
            const tr = document.createElement('tr');

            const isLate = task.atraso > 0;
            const statusBadge = isLate
                ? `<span class="status-badge danger"><i class="fa-solid fa-xmark"></i> Atrasado (${task.atraso}h)</span>`
                : `<span class="status-badge success"><i class="fa-solid fa-check"></i> No Prazo</span>`;

            tr.innerHTML = `
                <td><span class="order-badge">${index + 1}</span></td>
                <td><strong>${task.nome}</strong></td>
                <td><i class="fa-regular fa-clock" style="color:#94a3b8"></i> ${task.inicio}h &rarr; ${task.fim}h</td>
                <td>${task.deadline}h</td>
                <td>${statusBadge}</td>
            `;
            resultsTableBody.appendChild(tr);
        });
    }
});