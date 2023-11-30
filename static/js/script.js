let taskIdCounter = 0;

function addTask() {
    const tbody = document.getElementById('taskTableBody');
    const row = tbody.insertRow();

    // Готовность задачи
    const statusCell = row.insertCell();
    const statusButton = document.createElement("button");
    statusButton.className = "btn btn-outline-success";
    statusButton.textContent = "Выполнено";
    statusButton.onclick = function() {
        toggleTaskStatus(row, statusButton);
    };
    statusCell.appendChild(statusButton);


    // Название задачи
    const titleCell = row.insertCell();
    const titleInput = document.createElement("input");
    titleInput.type = "text";
    titleInput.className = "form-control";
    titleInput.placeholder = "Название задачи";
    titleInput.id = "taskTitle" + taskIdCounter;  // id
    titleInput.name = "taskTitle" + taskIdCounter; // name
    titleCell.appendChild(titleInput);

    // Описание задачи
    const descriptionCell = row.insertCell();
    const descriptionInput = document.createElement("textarea");
    descriptionInput.className = "form-control";
    descriptionInput.placeholder = "Описание задачи";
    descriptionCell.appendChild(descriptionInput);

    // Срок выполнения
    const deadlineCell = row.insertCell();
    const deadlineInput = document.createElement("input");
    deadlineInput.type = "date";
    deadlineInput.className = "form-control";
    deadlineCell.appendChild(deadlineInput);

    // Приоритет
    const priorityCell = row.insertCell();
    const prioritySelect = document.createElement("select");
    prioritySelect.className = "form-control";
    ["Высокий", "Средний", "Низкий"].forEach(priority => {
        const option = document.createElement("option");
        option.value = priority;
        option.textContent = priority;
        prioritySelect.appendChild(option);
    });
    priorityCell.appendChild(prioritySelect);
    
    // Тег
    const tagCell = row.insertCell();
    const tagInput = document.createElement("input");
    tagInput.type = "text";
    tagInput.className = "form-control";
    tagInput.placeholder = "Тег";
    tagCell.appendChild(tagInput);

    // Действия
    const actionsCell = row.insertCell();
    const deleteButton = document.createElement("button");
    deleteButton.className = "btn btn-danger";
    deleteButton.textContent = "Удалить";
    deleteButton.onclick = function() { deleteTask(row); };
    actionsCell.appendChild(deleteButton);

    taskIdCounter++
}


function deleteTask(row) {
    const tbody = document.getElementById('taskTableBody');
    tbody.removeChild(row);
}

function toggleTaskStatus(row, button) {
    const isCompleted = row.classList.contains("task-completed");
    if (isCompleted) {
        // Если задача была выполнена, изменяем ее на не выполненную
        row.classList.remove("task-completed");
        button.textContent = "Выполнено";
        button.className = "btn btn-outline-success";
    } else {
        // Если задача не была выполнена, изменяем ее на выполненную
        row.classList.add("task-completed");
        button.textContent = "Не выполнено";
        button.className = "btn btn-outline-secondary";
    }
}
