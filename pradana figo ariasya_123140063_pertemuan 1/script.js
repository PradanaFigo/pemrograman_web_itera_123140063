const taskName = document.getElementById('taskName');
const courseName = document.getElementById('courseName');
const deadline = document.getElementById('deadline');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');
const filterStatus = document.getElementById('filterStatus');
const filterCourse = document.getElementById('filterCourse');
const taskCount = document.getElementById('taskCount');

const editModal = document.getElementById('editModal');
const editName = document.getElementById('editName');
const editCourse = document.getElementById('editCourse');
const editDeadline = document.getElementById('editDeadline');
const saveEdit = document.getElementById('saveEdit');
const cancelEdit = document.getElementById('cancelEdit');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
let editIndex = null;

// Simpan ke localStorage
function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Render tugas
function renderTasks() {
  taskList.innerHTML = '';

  const status = filterStatus.value;
  const searchCourse = filterCourse.value.toLowerCase();

  const filtered = tasks.filter(t => {
    const statusMatch = status === 'all' ||
      (status === 'pending' && !t.completed) ||
      (status === 'completed' && t.completed);
    const courseMatch = t.course.toLowerCase().includes(searchCourse);
    return statusMatch && courseMatch;
  });

  filtered.forEach((task, index) => {
    const card = document.createElement('div');
    card.className = `task-card ${task.completed ? 'completed' : ''}`;

    card.innerHTML = `
      <div class="task-info">
        <h3>${task.name}</h3>
        <p>${task.course}</p>
        <p>Deadline: ${task.deadline}</p>
      </div>
      <div class="task-actions">
        <button onclick="toggleComplete(${index})">${task.completed ? 'Batal' : 'Selesai'}</button>
        <button onclick="openEditModal(${index})">Edit</button>
        <button onclick="deleteTask(${index})">Hapus</button>
      </div>
    `;

    taskList.appendChild(card);
  });

  const pendingCount = tasks.filter(t => !t.completed).length;
  taskCount.textContent = `Tugas Belum Selesai: ${pendingCount}`;
}

// Tambah tugas
addTaskBtn.addEventListener('click', () => {
  const name = taskName.value.trim();
  const course = courseName.value.trim();
  const date = deadline.value;

  if (!name || !course || !date) {
    alert('Isi semua field dengan benar!');
    return;
  }

  tasks.push({ name, course, deadline: date, completed: false });
  saveTasks();
  renderTasks();
  taskName.value = '';
  courseName.value = '';
  deadline.value = '';
});

// Toggle status
function toggleComplete(index) {
  tasks[index].completed = !tasks[index].completed;
  saveTasks();
  renderTasks();
}

// Hapus tugas
function deleteTask(index) {
  if (confirm('Hapus tugas ini?')) {
    tasks.splice(index, 1);
    saveTasks();
    renderTasks();
  }
}

// Edit modal
function openEditModal(index) {
  editIndex = index;
  editName.value = tasks[index].name;
  editCourse.value = tasks[index].course;
  editDeadline.value = tasks[index].deadline;
  editModal.style.display = 'flex';
}

saveEdit.addEventListener('click', () => {
  tasks[editIndex].name = editName.value;
  tasks[editIndex].course = editCourse.value;
  tasks[editIndex].deadline = editDeadline.value;
  saveTasks();
  renderTasks();
  editModal.style.display = 'none';
});

cancelEdit.addEventListener('click', () => {
  editModal.style.display = 'none';
});

// Tutup modal jika klik di luar konten
window.onclick = (e) => {
  if (e.target == editModal) editModal.style.display = 'none';
};

// Filter
filterStatus.addEventListener('change', renderTasks);
filterCourse.addEventListener('input', renderTasks);

// Inisialisasi
renderTasks();
