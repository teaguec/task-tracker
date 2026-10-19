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
    
def add():
    data = load_tasks()
    task = sys.argv[2]
    data.append({"task": task})
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)

def update():
    data = load_tasks()
    task = sys.argv[2]
    status = sys.argv[3]
    for item in data:
        if item["task"] == task:
            item["status"] = status
            break
    
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)

def delete():
    data = load_tasks()
    task = sys.argv[2]
    for item in data:
        if item["task"] == task:
            data.remove(item)
            break
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)

    

action = sys.argv[1].lower()

match action:
    case "add":
        add()
    case "update":
        update()
    case "delete":
        delete()