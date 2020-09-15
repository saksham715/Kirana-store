# Creating a to do list

todos = []

while True:
    ques = input('Do you want to add or delete the work from the list (Quit / Add / Delete) \n')
    if ques in ['a' or 'A' or 'add' or 'Add']:
        add = input('Add the work: \n')
        todos.append(add)
        print(todos)

    elif ques in ['d' or 'D' or 'Delete' or 'delete']:
        delete = int(input('Which work you want to delete. Type the index (0, 1, 2, 3 ....)'))
        todos.remove(todos[delete])
        print(todos)

    elif ques in ['q', 'Q', 'Quit', 'quit']:
        print(todos)
        break