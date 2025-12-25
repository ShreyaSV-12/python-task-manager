# Python Task Manager
# Description:Command-Line application to manage tasks

tasks=[]

def show_menu():
    print("\n---Task Manager--")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.exit")


def add_task():
    task=input("enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks)==0:
        print("no tasks available")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
        print("Total tasks:",len(tasks))


def delete_tasks():
    view_tasks()
    try:
        task_num=int(input("enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number" )
    except ValueError:
        print("Please enter a valid number")
        

while True:
    show_menu()
    choice=input("choose an option: ")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        delete_tasks()
    elif choice=="4":
        print("exiting task manager")
        break
    else:
        print("Invalid Choice.Try Again!")