dict_of_tasks={'0':{'name':'task 0','status':'to-do'}}

def add(x):
    global id
    id=1
    dict_of_tasks[str(id)]={'name':x,'status':'to-do'}
    id+=1

def list():
    print(dict_of_tasks)

def list_todo():
    for key in dict_of_tasks:
        if dict_of_tasks[key]['status']=='to-do':
            print(f"{key}: {dict_of_tasks[key]['name']}")

def list_done():
    for key in dict_of_tasks:
        if dict_of_tasks[key]['status']=='done':
            print(f"{key}: {dict_of_tasks[key]['name']}")

def list_in_progress():
    for key in dict_of_tasks:
        if dict_of_tasks[key]['status']=='in-progress':
            print(f"{key}: {dict_of_tasks[key]['name']}")

def update(x,y):
    dict_of_tasks[x]['name']=y

def delete(x):
    del dict_of_tasks[x]

def mark_done(x):
    dict_of_tasks[x]['status']='done'

def mark_in_progress(x):
    dict_of_tasks[x]['status']='in-progress'


while True:
    input_action=input().split()
    function=input_action[0]
    if function=='add':
        add(' '.join(input_action[1:]))
        print(input_action)
    elif function=='list':
        list()
    elif function=='list-todo':
        list_todo()
    elif function=='list-done':
        list_done()
    elif function=='list-in-progress':
        list_in_progress()
    elif function=='update':
        update(input_action[1],input_action[2])
    elif function=='delete':
        delete(input_action[1])
    elif function=='mark-done':
        mark_done(input_action[1])
    elif function=='mark-in-progress':
        mark_in_progress(input_action[1])


