tasks=[]

def addTask():
    task= input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks,start=1):
            print(f"Task #{index}. {task}")
            
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the task number to delete: "))-1
        if taskToDelete>=0 and taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task}' has been removed.")
            
        else:
            print(f"Task #{taskToDelete +1} was not found.")
    except:
        print("Invalid input.")

def clearList():
    if not tasks:
        print("There are no tasks to delete.")
    else:
        tasks.clear()
        print("All tasks have been deleted.")

if __name__== "__main__":
    print("Welcome to the To Do List application :) ")
    while(True):
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Clear all tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if(choice== "1"):
            addTask()
        elif(choice== "2"):
            deleteTask()
        elif(choice== "3"):
            listTasks()
        elif(choice == "4"):
            clearList()
        elif(choice== "5"):
            break;
        
        else:
            print("Invalid input. Please try again.")
            
    print("Goodboye !!")
    
        
    
