import json
import sys
import os
import datetime as dt

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
    data.append({"id": id, "task": task, "description": description, "createdAt": now})
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=4)

def update():
    data = load_tasks()
    task = sys.argv[2]
    property = sys.argv[3].lower()

    if property not in ["task", "description", "status"]:
        print("Invalid property. Try again")
    else:
        value = sys.argv[4]
        for item in data:
            if item["task"] == task:
                item[property] = value
                item["updatedAt"] = now
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

def show_list():
    data = load_tasks()
    print("TO DO LIST\n----------")
    for i in data:
        if i.get("status") is None:
            i["status"] = "null"
        print(i)



action = sys.argv[1].lower()
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