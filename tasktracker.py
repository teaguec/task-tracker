import json
import sys
import os
import datetime as dt

def usage():
    print("How to use this tool\n------------")
    print("Add a task: Enter python tasktracker.py add *taskname* *description*")
    print("Update a task: Enter python tasktracker.py update *id* *property* *value*")
    print("Delete a task: Enter python tasktracker.py delete *id*")
    print("List tasks: Enter python tasktracker.py list *command* (Note command can be 'all', 'todo', 'in-progress' or 'done')")

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
    description = sys.argv[3]
    try:   
        id = data[-1].get("id")
        id+=1
    except:
        id = 1
    data.append({"id": id, "task": task, "description": description, "status": "todo", "createdAt": now})
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Task added")

def update():
    data = load_tasks()
    id = id_check()
    property = sys.argv[3].lower()

    if property not in ["task", "description", "status"]:
        print("Invalid property. Try again")
    else:
        value = sys.argv[4]
        for item in data:
            if item["id"] == id:
                item[property] = value
                item["updatedAt"] = now
                break
        with open('file.json', 'w') as f:
                json.dump(data, f, indent=4)
        print("Task updated")
    

def delete():
    data = load_tasks()
    id = id_check()
    for item in data:
        if item["id"] == id:
            data.remove(item)
            break
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Task deleted")

def show_list():
    list_type = sys.argv[2]
    data = load_tasks()
    print("TO DO LIST\n----------")
    if list_type == "all":    
        for i in data:
            print(i)
    else:
        for i in data:
            if i["status"] == list_type:
                print(i)

def id_check():
    try:
        id = int(sys.argv[2])
        return id
    except Exception as e:
        print("ERROR:", e)
        sys.exit()

try:
    action = sys.argv[1].lower()
except Exception as e:
    print("ERROR:", e)
    usage()
    sys.exit()

now = str(dt.datetime.now().replace(microsecond=0))

match action:
    case "add":
        add()
    case "update":
        update()
    case "delete":
        delete()
    case "list":
        show_list()
    case _:
        usage()
