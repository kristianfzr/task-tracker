import sys
from datetime import datetime
import json
import os

filename = "tasks.json"

def list_tasks(filename, status):
    try: 
        with open(filename, "r") as file:
            tasks = json.load(file)
            
        if not tasks:
            print("Not tasks found.")
            return
        
        id_width = max(t["id"] for t in tasks)
        task_width = max(len(t["description"]) for t in tasks)
        status_width = max(len(t["status"]) for t in tasks)
        
        print(f"{'ID':<{id_width}} {'Task':<{task_width}} {'Status':<{status_width}} ")
        print("-" * (id_width + task_width + status_width + 4))
        
        status = status.lower()
        
        tasks = [t for t in tasks if status == "" or t["status"].lower() == status]

        for task in tasks:
            if status in ("", "todo", "in-progress"):
                print(f"{task['id']:<{id_width}} {task['description']:<{task_width}} {task['status']:<{status_width}}")
            
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Inalid JSON file.")
        
def add_task(filename, description):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
        
    next_id = (max((int(t["id"]) for t in tasks), default=0)) + 1
    task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
     
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
        
    tasks.append(task)
    
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    
    print(f"Task added : {task['description']}")
    
def delete_task(filename, id: int):
    with open(filename, 'r') as file:
        tasks = json.load(file)
        
    tasks = [t for t in tasks if int(t["id"]) != int(id)]
    
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)    
       
def main():
    command = sys.argv[1]
    
    if len(sys.argv) > 1:
        if command == "list":
            arg = sys.argv[2] if len(sys.argv) > 2 else ""
            list_tasks(filename, arg)
        elif command == "add":
            description_input = sys.argv[2:]
            description = (" ").join(description_input)
            
            add_task(filename, description)
        elif command == "delete":
            delete_task(filename, sys.argv[2])
            
if __name__ == "__main__":
    main()