import datetime

print("Welcome to 'TEXT USER INETERFACE' of To do List app")
def tuiInstructions():
    print("ENTER 'A' TO ADD A TASK TO THE LIST")
    print("ENTER 'V' TO VIEW YOUR TASKS")
    print("ENTER 'Q' TO EXIT")

task_id =[]
task =[]
date=[]
#def setTaskid(taskId):

def setTask():
    taskIn  = input('Enter your task')
    task.append(taskIn)
def setDate():
    date.append(datetime.datetime.now())
#def add_task():
def setTaskID(taskId):
    task_id.append(taskId)

tuiInstructions()
user = input()

while(user!='q' or user!='Q'):
    
    if(user=='A'or user=='a'):
        setTask()
        setDate()
        setTaskID(len(setTask))
    elif(user=='V'or user=='v'):
        for i in range(0,len(task_id)):
            print("Task ID:"+task_id[i]+"\nTask Date: "+date[i]+"\nTask:"+task)
            print("###########################################################")
    else:
        print("Wrong input")

    

