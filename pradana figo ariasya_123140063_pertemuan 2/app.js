class Storage {
  static save(key, value) { localStorage.setItem(key, JSON.stringify(value)); }
  static load(key) { return JSON.parse(localStorage.getItem(key)) || []; }
  static saveSetting(key, value) { localStorage.setItem(key, JSON.stringify(value)); }
  static loadSetting(key, fallback) { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; }
}

class Task {
  constructor(name, done = false, id = Date.now(), createdAt = new Date().toISOString()) {
    this.id = id;
    this.name = name;
    this.done = done;
    this.createdAt = createdAt;
  }
}

class Schedule {
  constructor(text, id = Date.now(), createdAt = new Date().toISOString()) {
    this.id = id;
    this.text = text;
    this.createdAt = createdAt;
  }
}

const tasks = Storage.load('tasks').map(t => new Task(t.name, t.done, t.id, t.createdAt));
const schedules = Storage.load('schedules').map(s => new Schedule(s.text, s.id, s.createdAt));

const el = id => document.getElementById(id);
const fmtDate = iso => new Date(iso).toLocaleString('id-ID');
const saveAll = () => { Storage.save('tasks', tasks); Storage.save('schedules', schedules); };

const updateTasksUI = () => {
  saveAll();
  renderTasks(currentFilter);
};

const updateSchedulesUI = () => {
  saveAll();
  renderSchedules();
};

const renderStats = () => {
  const total = tasks.length;
  const done = tasks.filter(t => t.done).length;
  const active = total - done;
  el('totalTasks').textContent = total;
  el('doneTasks').textContent = done;
  el('activeTasks').textContent = active;
  const percent = total ? Math.round((done / total) * 100) : 0;
  el('progressBar').style.width = `${percent}%`;
  el('progressText').textContent = `${percent}% selesai`;
};

const renderTasks = (filter = 'all') => {
  const container = el('taskList');
  let list = tasks;
  if (filter === 'active') list = tasks.filter(t => !t.done);
  if (filter === 'done') list = tasks.filter(t => t.done);
  if (!list.length) { container.innerHTML = '<div class="muted">Belum ada tugas</div>'; renderStats(); return; }

  container.innerHTML = list.map(t => `
    <div class="list-item" data-id="${t.id}">
      <div class="item-left">
        <div class="checkbox" onclick="toggleDoneTask(${t.id})">${t.done ? '✓' : ''}</div>
        <div>
          <div style="text-decoration:${t.done ? 'line-through' : 'none'}">${t.name}</div>
          <div class="item-meta">Ditambahkan: ${fmtDate(t.createdAt)}</div>
        </div>
      </div>
      <div class="actions">
        <button class="btn-sm btn-edit" onclick="editTask(${t.id})">✎</button>
        <button class="btn-sm btn-delete" onclick="deleteTask(${t.id})">🗑</button>
      </div>
    </div>
  `).join('');
  renderStats();
};

const renderSchedules = () => {
  const container = el('scheduleList');
  if (!schedules.length) { container.innerHTML = '<div class="muted">Belum ada jadwal</div>'; return; }
  container.innerHTML = schedules.map(s => `
    <div class="list-item" data-id="${s.id}">
      <div class="item-left">
        <div>
          <div>${s.text}</div>
          <div class="item-meta">Ditambahkan: ${fmtDate(s.createdAt)}</div>
        </div>
      </div>
      <div class="actions">
        <button class="btn-sm btn-edit" onclick="editSchedule(${s.id})">✎</button>
        <button class="btn-sm btn-delete" onclick="deleteSchedule(${s.id})">🗑</button>
      </div>
    </div>
  `).join('');
};

const addTask = () => {
  const v = el('taskInput').value.trim();
  if (!v) return;
  tasks.unshift(new Task(v));
  el('taskInput').value = '';
  updateTasksUI();
};

const deleteTask = (id) => {
  const idx = tasks.findIndex(t => t.id === id);
  if (idx === -1) return;
  if (!confirm('Hapus tugas ini?')) return;
  tasks.splice(idx, 1);
  updateTasksUI();
};

const editTask = (id) => {
  const t = tasks.find(x => x.id === id);
  if (!t) return;
  const nv = prompt('Edit tugas:', t.name);
  if (nv === null) return;
  t.name = nv.trim() || t.name;
  updateTasksUI();
};

const toggleDoneTask = (id) => {
  const t = tasks.find(x => x.id === id);
  if (!t) return;
  t.done = !t.done;
  updateTasksUI();
};

const addSchedule = () => {
  const v = el('scheduleInput').value.trim();
  if (!v) return;
  schedules.unshift(new Schedule(v));
  el('scheduleInput').value = '';
  updateSchedulesUI();
};

const deleteSchedule = (id) => {
  const idx = schedules.findIndex(s => s.id === id);
  if (idx === -1) return;
  if (!confirm('Hapus jadwal ini?')) return;
  schedules.splice(idx, 1);
  updateSchedulesUI();
};

const editSchedule = (id) => {
  const s = schedules.find(x => x.id === id);
  if (!s) return;
  const nv = prompt('Edit jadwal (Format: Matkul • Hari • Jam):', s.text);
  if (nv === null) return;
  s.text = nv.trim() || s.text;
  updateSchedulesUI();
};

let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', () => {
  renderTasks();
  renderSchedules();
  renderStats();
  renderDateTime();

  el('addTaskBtn').addEventListener('click', addTask);
  el('addScheduleBtn').addEventListener('click', addSchedule);
  el('taskInput').addEventListener('keydown', e => e.key === 'Enter' && addTask());
  el('scheduleInput').addEventListener('keydown', e => e.key === 'Enter' && addSchedule());

  document.querySelectorAll('.filter').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.filter;
      renderTasks(currentFilter);
    });
  });

  const dark = Storage.loadSetting('darkMode', false);
  el('darkToggle').checked = dark;
  applyDark(dark);
  el('darkToggle').addEventListener('change', (e) => {
    Storage.saveSetting('darkMode', e.target.checked);
    applyDark(e.target.checked);
  });

  setInterval(renderDateTime, 1000);
});

function renderDateTime() {
  const now = new Date();
  el('clock').textContent = now.toLocaleTimeString('id-ID');
  el('dateText').textContent = now.toLocaleDateString('id-ID');
}

function applyDark(on) {
  if (on) {
    document.documentElement.style.setProperty('--bg', 'linear-gradient(180deg,#0f1724 0%,#071033 100%)');
    document.documentElement.style.setProperty('--text', '#e6eefc');
    document.documentElement.style.setProperty('--muted', '#b6c0d9');
    document.documentElement.style.setProperty('--glass', 'rgba(255,255,255,0.04)');
  } else {
    document.documentElement.style.setProperty('--bg', 'linear-gradient(180deg,#eef3ff 0%, #f6f8ff 100%)');
    document.documentElement.style.setProperty('--text', '#0f1530');
    document.documentElement.style.setProperty('--muted', '#6b7490');
    document.documentElement.style.setProperty('--glass', 'rgba(255,255,255,0.75)');
  }
}

window.toggleDoneTask = toggleDoneTask;
window.editTask = editTask;
window.deleteTask = deleteTask;
window.editSchedule = editSchedule;
window.deleteSchedule = deleteSchedule;
