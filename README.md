# 📝 Task Manager CLI

A simple **Python CLI To-Do application** that lets you add, edit, delete, view, and manage tasks stored in a JSON file.

---

## Getting Started

Follow the steps below to set up and run the app locally.

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

* On **Linux / macOS**:

  ```bash
  source venv/bin/activate
  ```

* On **Windows (PowerShell)**:

  ```powershell
  .\venv\Scripts\activate
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python3 main.py
```

---

## Project Structure

```
.
├── main.py               # Entry point
├── options/              # Modules for task operations
│   ├── add_tasks.py
│   ├── delete_task.py
│   ├── edit_task.py
│   ├── export_tasks.py
│   ├── load_save_tasks.py
│   └── view_tasks.py
├── requirements.txt      # Python dependencies
└── tasks.json            # Task data (auto-saved)
```

---

That’s it! You can now manage tasks directly from your terminal.
