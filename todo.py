
def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
    
    
def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
            
            
            
def main():
    filename = "todo.txt"
    tasks = load_tasks(filename)
    
    print("Your list:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
    else: 
        print("Пока пусто")
        
        
    print("\nДобавим новые задачи (оставь пустую строку для завершения):")
    while True:
        new_task = input("➕ Новая задача: ")
        if new_task == "":
            break
        tasks.append(new_task)
    save_tasks(tasks, filename)
    print("\n✅ Список обновлён и сохранён!")

if __name__ == "__main__":
    main()
