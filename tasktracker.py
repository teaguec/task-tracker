import json
import sys
import os

def load_tasks():
    if os.path.exists('file.json'):
        with open('file.json', 'r') as f:
            contents = json.load(f)
            return contents
    else:
        with open('file.json', 'w') as f:
            f.write("[]")
            return []
    
def add(task, status):
    data = load_tasks()
    data.append({"task": task, "status": status})
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)

def update(task, status):
    data = load_tasks()
    for item in data:
        if item["task"] == task:
            item["status"] = status
            break
    
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)
            
    

    

action = sys.argv[1].lower()
task = sys.argv[2]
status = sys.argv[3]


#if action == "add":
   # f(task, 'a')
match action:
    case "add":
        add(task, status)
    case "update":
        update(task, status)