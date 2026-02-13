import os

tasks_file = 'tasks.txt'

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_tasks(tasks):
    with open(tasks_file, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def add_task(tasks):
    task = input('Enter new task: ').strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print('Task added.')
    else:
        print('Empty task not added.')

def remove_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input('Enter task number to remove: ')) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f'Task removed: {removed}')
        else:
            print('Invalid task number.')
    except ValueError:
        print('Please enter a valid number.')

def view_tasks(tasks):
    if not tasks:
        print('No tasks found.')
    else:
        print('\nYour Tasks:')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        print()

def main():
    tasks = load_tasks()
    while True:
        print('--- To-Do List Manager ---')
        print('1. View Tasks')
        print('2. Add Task')
        print('3. Remove Task')
        print('4. Exit')
        choice = input('Select an option (1-4): ').strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()
