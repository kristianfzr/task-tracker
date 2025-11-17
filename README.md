# Task Tracker

A simple command-line task tracker built as a learning project.

## About

This is an MVP (Minimum Viable Product) created to practice coding and learn software development concepts. It's not meant to be a perfect solution, but rather a working one that demonstrates core functionality.

## Installation

### Option 1: Direct Python Execution
Clone the repository and run directly:
```bash
git clone https://github.com/kristianfzr/task-tracker.git
cd task-tracker
python3 index.py list
```

### Option 2: Install as CLI Tool
Install it globally so you can use `task-tracker` command from anywhere:

```bash
# Clone the repository
git clone https://github.com/kristianfzr/task-tracker.git
cd task-tracker

# Install in development mode
pip install -e .

# Now you can use it anywhere
task-tracker list
```

### Option 3: Shell Alias (Quick Setup)
Add to your `~/.zshrc` or `~/.bashrc`:
```bash
alias task-tracker='python3 /path/to/task-tracker/index.py'
```
Then reload your shell: `source ~/.zshrc`

## Usage

Once installed, you can use the following commands:

```bash
# List all tasks
task-tracker list

# List tasks by status
task-tracker list done
task-tracker list todo
task-tracker list in-progress

# Add a new task
task-tracker add "Your task description"

# Update a task
task-tracker update <id> "Updated description"

# Delete a task
task-tracker delete <id>
```

**Note:** If you haven't installed it as a CLI tool, replace `task-tracker` with `python3 index.py` in the commands above.

## Learning Goals

- Working with JSON files
- Command-line argument parsing
- Basic CRUD operations
- Python file I/O and data structures
- Python packaging and distribution

