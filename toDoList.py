import datetime
import os
os.system('clear')

def tuiInstructions():
    print("ENTER 'A' TO ADD A TASK TO THE LIST")
    print("ENTER 'V' TO VIEW YOUR TASKS")
    print("ENTER 'Q' TO EXIT")
    
def setTask():
    taskIn  = input('Enter your task name : ')
    task.append(taskIn)
def setDate():
    date.append(datetime.datetime.now())

def setTaskID(taskId):
    task_id.append(taskId)

print("Welcome to 'TEXT USER INETERFACE' of To do List app") 
print("_____________________________________________________")

task_id =[]
task =[]
date=[]

user = 'g'

while user.lower()!='q':
    tuiInstructions()
    user = input()
    if(user.lower() =='a'):
        setTask()
        setDate()
        setTaskID((len(task)))
        

    elif(user.lower()=='v'):
        for i in range(0,len(task_id)):
            print("Task ID:"+str(task_id[i])+"\nTask Date: "+str(date[i])+"\nTask:"+task[i])
            print("_____________________________________________________________________")
            
    elif(user.lower=='q'):
        break

    else:
        print("Wrong input")
    
   

    

