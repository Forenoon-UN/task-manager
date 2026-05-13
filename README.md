

```markdown
# 📝 Task Manager — نظام إدارة المهام

A command-line Task Manager built with **Python** using the **MVC Architecture**.

---

## 🏗️ Architecture: MVC (Model-View-Controller)

| Layer | File | Responsibility |
|-------|------|----------------|
| **Model** | `models.py` | User and Task classes — data only |
| **Controller** | `controller.py` | Business logic (add, edit, delete, complete) |
| **View** | `view.py` | CLI interface — user interaction |

---

## ✨ Features

- 🔐 User login
- ➕ Add a new task
- 📋 View all tasks
- ✏️ Edit a task
- 🗑️ Delete a task
- ✔️ Mark task as completed

---

## ▶️ How to Run

```bash
python view.py
```

**Default credentials:**
- Username: `admin`
- Password: `1234`

---

## 📁 Project Structure

```
task_manager/
├── models.py       # Model Layer — Data
├── controller.py   # Controller Layer — Logic  
└── view.py         # View Layer — Interface
```

---

## 🎓 Course
Software Architecture — MVC Pattern Implementation
```
 
