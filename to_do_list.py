
tasks=[]
def addTask():
    task=input("please enter your task :")
    tasks.append(task)
    print(f"Task '{task}' added to the list")
def listTask():
    if not tasks:
        print("there are no task in this list currently")
    else:
        print("current task.")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("please enter how many task do you wont to delete :"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"task {taskToDelete} has been removed.")

        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("invalid input")

if __name__=="__main__":
    # create a loop for run to do list terminal based app
    print("Welcome to to do list app ")
    while True:
        print("\n")
        print("please select from this option what you wont to do:")
        print("-----------------------------------------------------")
        print("1. Add a new task")
        print("2.Delete a task")
        print("3. list of tasks")
        print("4 quit")
        choice=input("enter your choice from givin option :")
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice=="4"):
            break
        else:
            print("invlaid input. please try again")
print("Thank you for using TO DO LIST")