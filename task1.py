# task 1
# To-do list Application

# main look
print(' *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('        WELCOME TO-DO LIST APPLICATION      ')
print(' *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

# Initialize an empty list to store tasks
to_do_list = []


# Add a task to the list
def add_task():
    print("Great! Let's start a new task.")
    new_task = input('Enter a task:')
    to_do_list.append(new_task)
    print("You've got it! Task successfully added.")


# Update the task at the specified index
def update_task():
    if not to_do_list:
        print("Oops! You can't update a task because your task list is empty.")

    else:
        task_update = input('Enter an updated task: ')
        task_index = int(input('Enter index for which you want to replace the task: ')) - 1
        if 0 <= task_index < len(to_do_list):
            to_do_list[task_index] = task_update
            print('Your task has been successfully updated!')
        else:
            print('First you have to add the task.')
            print('Invalid index. Task not updated.')


# Remove the task at the specified index
def delete_task():
    if not to_do_list:
        print("No tasks in the to-do list. First you have to add the task")

    else:
        task_index = int(input('Enter index for which you want to remove the task:')) - 1
        if 0 <= task_index < len(to_do_list):
            del to_do_list[task_index]
            print('Task successfully deleted.')
        else:
            print('Select the right index!')


# main loop
try:
    while True:
        print()
        print('MENU:')
        print("1. Add a New Task")
        print("2. Update Task")
        print("3. Delete Tasks")
        print("4. View Your Task List")
        print("5. Exit")

        choice = int(input('Enter the number of your chosen option:'))
        if choice == 1:
            add_task()

        elif choice == 2:
            update_task()

        elif choice == 3:
            delete_task()

        elif choice == 4:
            # View the list of tasks
            print("Let's review your existing tasks!")

            if not to_do_list:
                print("Currently, No tasks in the to-do list.")

            else:
                print("=" * 30)
                print("{:<10} {:<30}".format("S.NO", "TASK'S"))
                print("=" * 30)
                for index, task in enumerate(to_do_list, start=1):
                    print("{:<10} {:<30}".format(index, task))
            # print('LIST OF TASK:\n', to_do_list)

        elif choice == 5:
            # Exit the application
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Oops! That's not a valid choice!! Please select a valid option number")

# exception handling
except ValueError:
    print('Invalid Input!! PLease enter a integer.')
